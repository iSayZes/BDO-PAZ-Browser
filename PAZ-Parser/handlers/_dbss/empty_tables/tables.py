from __future__ import annotations

# Tables the client ships with a u32 count of 0 (docs/file-formats/empty_dbss.md).
# Each main file and its offset companion is only that count;
# itemcouponreward.dbss has 12 zero bytes after it. itemcouponrewardoffset.dbss
# declares 4 entries and has its own raw view in _dbss/itemcouponreward/.
EMPTY_TABLES: tuple[str, ...] = (
    "alchemystatus.dbss",
    "alchemystatusoffset.dbss",
    "buffcondition.dbss",
    "buffconditionoffset.dbss",
    "cashforui.dbss",
    "cashforuioffset.dbss",
    "chinaspawnoption.dbss",
    "chinaspawnoptionoffset.dbss",
    "grenadedata.dbss",
    "grenadedataoffset.dbss",
    "installation.dbss",
    "installationoffset.dbss",
    "itemcouponreward.dbss",
    "petmarketsetting.dbss",
    "petmarketsettingoffset.dbss",
    "petset.dbss",
    "petsetoffset.dbss",
    "servantcategory.dbss",
    "servantcategoryoffset.dbss",
    "worldquest.dbss",
)
