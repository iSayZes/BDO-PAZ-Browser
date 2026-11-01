"""Pearl Shop category names: LOC type 51, keyed by the category path.

`(51, main, middle, small, 0)` names one category; a main category writes
middle `65535` and small `255`, a middle category small `255`. Client 3482
also keeps rows with middle or small `0`, which no category of the file
uses. See docs/file-formats/dbss/cashproductcategory_dbss.md.
"""

from __future__ import annotations

from _common.inline_text import decode_inline_text
from _common.loc import loc_lookup
from _common.pa_text import strip_pa_tags
from .parser import NO_MIDDLE, NO_SMALL

LOC_CASH_CATEGORY = 51
# The LOC type 51 main key of the file head's all-categories name: row 99 of
# the client 1784 `CouponCategory_Table` sheet holds the same Korean text.
ALL_CATEGORIES_KEY = 99
# `price_type`: the `PriceType` text of the client 1784 sheet per value.
PRICE_TYPE_NAMES = ("Silver", "Cash", "Pearl", "Mileage")


def category_name_tagged(main_key: int, middle_key: int | None = None, small_key: int | None = None) -> str:
    """LOC type 51 name of a category with its PA tags, or ''."""
    middle = NO_MIDDLE if middle_key is None else middle_key
    small = NO_SMALL if small_key is None else small_key
    return loc_lookup(LOC_CASH_CATEGORY, main_key, middle, small).strip()


def category_label_tagged(record: dict) -> str:
    """A category record's name: LOC type 51, else its Korean name (line breaks decoded)."""
    return (
        category_name_tagged(record["main_key"], record["middle_key"], record["small_key"])
        or decode_inline_text(record["name_kr"]).strip()
    )


def category_path_text(main_key: int, middle_key: int | None, small_key: int | None) -> str:
    """`Costumes(Outfits(Permanent Outfits))`, the shape of the coupon's Korean category text, or ''.

    Empty when LOC lacks any of the names, so the caller can fall back to
    the Korean text the table stores.
    """
    names = [category_name_tagged(main_key)]
    if middle_key is not None:
        names.append(category_name_tagged(main_key, middle_key))
    if small_key is not None:
        names.append(category_name_tagged(main_key, middle_key, small_key))
    plain = [" ".join(strip_pa_tags(name).split()) for name in names]
    if not all(plain):
        return ""
    text = plain[-1]
    for name in reversed(plain[:-1]):
        text = f"{name}({text})"
    return text
