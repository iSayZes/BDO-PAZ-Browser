"""Pearl Shop product names and descriptions from LOC type 50.

Keyed `(product_id, 0, service code, field)`: field 0 is the product name and
3 the description, both with their `<PAColor>` tags. The service code in
`str_id3` is the same on nearly every product of one LOC file (12 in the en,
de, fr and sp files, 8 in ru), and a few products also or only have rows
under another code. The code most products use wins, else the lowest one.
See "Type 50" in docs/file-formats/other/languagedata_loc.md.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from _common.loc import loc_type_entries

LOC_CASH_PRODUCT = 50
_FIELD_NAME = 0
_FIELD_DESCRIPTION = 3


@dataclass(frozen=True)
class ProductText:
    """A product's tagged name and description; "" where LOC has no row."""

    name: str
    description: str


def product_texts() -> dict[int, ProductText]:
    """Product ID -> its LOC text, or empty when LOC is not loaded."""
    entries = loc_type_entries(LOC_CASH_PRODUCT)
    codes_by_product: dict[int, set[int]] = {}
    for _, product_id, _, code, _ in entries:
        codes_by_product.setdefault(product_id, set()).add(code)
    if not codes_by_product:
        return {}

    code_counts = Counter(code for codes in codes_by_product.values() for code in codes)
    main_code = code_counts.most_common(1)[0][0]
    texts: dict[int, ProductText] = {}
    for product_id, codes in codes_by_product.items():
        code = main_code if main_code in codes else min(codes)
        texts[product_id] = ProductText(
            name=entries.get((LOC_CASH_PRODUCT, product_id, 0, code, _FIELD_NAME), "").strip(),
            description=entries.get((LOC_CASH_PRODUCT, product_id, 0, code, _FIELD_DESCRIPTION), "").strip(),
        )
    return texts
