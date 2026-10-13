//! The BDO payload decompressor, a port of `unpack_python` in
//! `paz/bdo_decompress.py`. The Python version is the reference: this file
//! follows it step by step, with the same names and error codes, and
//! `tests/test_decompress_native.py` checks the two give the same bytes.
//!
//! The input comes from a `.paz` file, so every read and write is range
//! checked and a bad payload returns an error code. Nothing here may panic:
//! PyO3 raises a panic as `PanicException`, which `except Exception` misses.

/// Bytes a literal run copies, indexed by the group header's low 4 bits.
/// Only even indices are reached: an odd one means a back-reference.
const LITERAL_LENGTHS: [i64; 16] = [4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0];

pub enum UnpackError {
    /// The negative code `unpack_python` returns for the same input.
    Code(i32),
    /// The output buffer could not be allocated.
    OutOfMemory,
}

/// Decompresses `data[input_start..input_end]` into `decompressed_length`
/// bytes. The result is shorter when the stream ends early, as in Python.
pub fn unpack(
    data: &[u8],
    input_start: usize,
    input_end: usize,
    decompressed_length: usize,
) -> Result<Vec<u8>, UnpackError> {
    let input = &data[..input_end.min(data.len())];
    let mut output: Vec<u8> = Vec::new();
    output
        .try_reserve_exact(decompressed_length)
        .map_err(|_| UnpackError::OutOfMemory)?;
    output.resize(decompressed_length, 0);
    let written =
        unpack_core(input, to_index(input_start), &mut output).map_err(UnpackError::Code)?;
    output.truncate(written);
    Ok(output)
}

/// Positions are signed, as in Python: an empty output has its last index at -1.
fn to_index(value: usize) -> i64 {
    i64::try_from(value).unwrap_or(i64::MAX)
}

fn unpack_core(input: &[u8], input_start: i64, output: &mut [u8]) -> Result<usize, i32> {
    let last_input = to_index(input.len()) - 1;
    let last_output = to_index(output.len()) - 1;
    let literal_end = (last_output - 10).max(0);
    let mut input_pos = input_start;
    let mut output_pos: i64 = 0;
    let mut group_header: u32 = 1;

    loop {
        // One bit of the group header per block.
        loop {
            if group_header == 1 {
                if input_pos + 3 > last_input {
                    return Err(-1);
                }
                group_header = read_u32(input, input_pos).ok_or(-1)?;
                input_pos += 4;
            }

            if input_pos + 3 > last_input {
                return Err(-2);
            }
            let block_header = read_u32(input, input_pos).ok_or(-2)?;

            if group_header & 1 == 0 {
                break; // literal run
            }

            let (repeat, length, header_length) = decode_back_reference(block_header);
            input_pos += header_length;

            // C++ unsigned arithmetic for the length bound, as in Python.
            let remaining = (last_output - output_pos - 3) & 0xFFFF_FFFF;
            if output_pos - repeat < 0 || repeat < 3 || length > remaining {
                return Err(-3);
            }
            copy_back_reference(output, output_pos, repeat, length).ok_or(-3)?;
            group_header >>= 1;
            output_pos += length;
        }

        if output_pos >= literal_end {
            break;
        }
        let length = LITERAL_LENGTHS[(group_header & 0xF) as usize];
        copy_literal(input, input_pos, output, output_pos, length).ok_or(-2)?;
        group_header >>= length;
        output_pos += length;
        input_pos += length;
    }

    if output_pos <= last_output {
        return copy_tail(input, output, input_pos, output_pos, group_header);
    }
    usize::try_from(output_pos).map_err(|_| -3)
}

/// (repeat distance, copy length, block header bytes) for the encoding the
/// low 2 bits pick.
fn decode_back_reference(block_header: u32) -> (i64, i64, i64) {
    let header = i64::from(block_header);
    match header & 0x03 {
        0x03 if header & 0x7F == 3 => (header >> 15, ((header >> 7) & 0xFF) + 3, 4),
        0x03 => ((header >> 7) & 0x1FFFF, ((header >> 2) & 0x1F) + 2, 3),
        0x02 => ((header & 0xFFFF) >> 6, ((header >> 2) & 0xF) + 3, 2),
        0x01 => ((header & 0xFFFF) >> 2, 3, 2),
        _ => ((header & 0xFF) >> 2, 3, 1),
    }
}

/// Copies byte by byte forward, so a source overlapping the destination
/// repeats its first `repeat` bytes.
fn copy_back_reference(output: &mut [u8], output_pos: i64, repeat: i64, length: i64) -> Option<()> {
    let start = usize::try_from(output_pos).ok()?;
    let end = start.checked_add(usize::try_from(length).ok()?)?;
    let source = start.checked_sub(usize::try_from(repeat).ok()?)?;
    if end > output.len() {
        return None;
    }
    if repeat >= length {
        output.copy_within(source..source + (end - start), start);
    } else {
        for index in start..end {
            output[index] = output[index - (start - source)];
        }
    }
    Some(())
}

fn copy_literal(
    input: &[u8],
    input_pos: i64,
    output: &mut [u8],
    output_pos: i64,
    length: i64,
) -> Option<()> {
    let length = usize::try_from(length).ok()?;
    let source = slice_at(input, input_pos, length)?;
    let start = usize::try_from(output_pos).ok()?;
    output
        .get_mut(start..start.checked_add(length)?)?
        .copy_from_slice(source);
    Some(())
}

/// The last bytes, one at a time, until the output is full.
fn copy_tail(
    input: &[u8],
    output: &mut [u8],
    mut input_pos: i64,
    mut output_pos: i64,
    mut group_header: u32,
) -> Result<usize, i32> {
    let input_end = to_index(input.len());
    let last_output = to_index(output.len()) - 1;
    loop {
        if group_header == 1 {
            input_pos += 4;
            group_header = 0x8000_0000;
        }

        if input_pos >= input_end {
            return Err(-4);
        }

        let byte = *slice_at(input, input_pos, 1)
            .and_then(|bytes| bytes.first())
            .ok_or(-4)?;
        let target = usize::try_from(output_pos)
            .ok()
            .and_then(|index| output.get_mut(index))
            .ok_or(-4)?;
        *target = byte;
        output_pos += 1;
        input_pos += 1;
        group_header >>= 1;

        if output_pos > last_output {
            return usize::try_from(output_pos).map_err(|_| -4);
        }
    }
}

fn slice_at(data: &[u8], pos: i64, length: usize) -> Option<&[u8]> {
    let start = usize::try_from(pos).ok()?;
    data.get(start..start.checked_add(length)?)
}

fn read_u32(data: &[u8], pos: i64) -> Option<u32> {
    let bytes: [u8; 4] = slice_at(data, pos, 4)?.try_into().ok()?;
    Some(u32::from_le_bytes(bytes))
}
