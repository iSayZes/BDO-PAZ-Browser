//! The ICE round loop, a port of `crypt_blocks_numpy` in `paz/bdo_ice.py`.
//! The key schedule and S-boxes stay in Python, built once; this gets the
//! subkeys and the four S-boxes and runs the Feistel rounds per block.
//! `tests/test_payload_decode.py` checks the two give the same bytes.

pub const SBOX_ENTRIES: usize = 1024;
const SBOX_BYTES: usize = 4 * SBOX_ENTRIES * 4;
const SBOX_INDEX_MASK: u32 = 0x3FF;
// Subkeys are 20 bits; larger ones would index past the S-boxes.
const SUBKEY_LIMIT: u32 = 1 << 20;
const BLOCK_SIZE: usize = 8;

pub type Subkey = (u32, u32, u32);

pub enum CryptError {
    Invalid(String),
    OutOfMemory,
}

/// `data` with every 8-byte block run through the rounds in `subkeys` order.
/// `sbox` is S-boxes 0 to 3, 1024 little-endian u32 each.
pub fn crypt(data: &[u8], subkeys: &[Subkey], sbox: &[u8]) -> Result<Vec<u8>, CryptError> {
    if !data.len().is_multiple_of(BLOCK_SIZE) {
        return Err(CryptError::Invalid(format!(
            "ICE input must be a multiple of 8 bytes, got {}.",
            data.len()
        )));
    }
    if subkeys
        .iter()
        .any(|&(k0, k1, k2)| k0 >= SUBKEY_LIMIT || k1 >= SUBKEY_LIMIT || k2 >= SUBKEY_LIMIT)
    {
        return Err(CryptError::Invalid(
            "ICE subkeys must be 20-bit values.".into(),
        ));
    }
    let sboxes = read_sboxes(sbox)?;

    let mut output: Vec<u8> = Vec::new();
    output
        .try_reserve_exact(data.len())
        .map_err(|_| CryptError::OutOfMemory)?;
    for block in data.as_chunks::<BLOCK_SIZE>().0 {
        let left = u32::from_be_bytes([block[0], block[1], block[2], block[3]]);
        let right = u32::from_be_bytes([block[4], block[5], block[6], block[7]]);
        let (first, second) = crypt_block(left, right, subkeys, &sboxes);
        output.extend_from_slice(&first.to_be_bytes());
        output.extend_from_slice(&second.to_be_bytes());
    }
    Ok(output)
}

/// Each round sets (l, r) to (r, l ^ F(r)); the halves come out swapped.
fn crypt_block(
    mut left: u32,
    mut right: u32,
    subkeys: &[Subkey],
    sboxes: &[[u32; SBOX_ENTRIES]; 4],
) -> (u32, u32) {
    for &(k0, k1, k2) in subkeys {
        // F(r): expand r to two 20-bit halves, salt-permute them with k2,
        // key them with k0 and k1, then look up the four S-boxes.
        let tl = ((right >> 16) & 0x3FF) | (right.rotate_right(14) & 0xFFC00);
        let tr = (right & 0x3FF) | ((right << 2) & 0xFFC00);
        let mut al = k2 & (tl ^ tr);
        let ar = al ^ tr ^ k1;
        al ^= tl ^ k0;
        let f = sboxes[0][sbox_index(al >> 10)]
            | sboxes[1][sbox_index(al)]
            | sboxes[2][sbox_index(ar >> 10)]
            | sboxes[3][sbox_index(ar)];
        (left, right) = (right, left ^ f);
    }
    (right, left)
}

fn sbox_index(value: u32) -> usize {
    (value & SBOX_INDEX_MASK) as usize
}

fn read_sboxes(sbox: &[u8]) -> Result<[[u32; SBOX_ENTRIES]; 4], CryptError> {
    if sbox.len() != SBOX_BYTES {
        return Err(CryptError::Invalid(format!(
            "ICE S-boxes must be {SBOX_BYTES} bytes, got {}.",
            sbox.len()
        )));
    }
    let mut sboxes = [[0u32; SBOX_ENTRIES]; 4];
    for (index, chunk) in sbox.as_chunks::<4>().0.iter().enumerate() {
        sboxes[index / SBOX_ENTRIES][index % SBOX_ENTRIES] = u32::from_le_bytes(*chunk);
    }
    Ok(sboxes)
}
