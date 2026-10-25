"""Trading EXP of one sold trade item at 1,000 distance.

`CalcTradeSellRewards` in a private server's server dump on client 1784
scales `trade_exp` by a distance factor that is 1.0 at 1,000 distance, then
by the item's `GetSellingTradeExpRate` in millionths, cutting off the
fraction and keeping at least 1 EXP after each step. The formula and the
readings that confirm it are in docs/file-formats/bss/tradeexperiencess_bss.md.
"""

from __future__ import annotations


# GetSellingTradeExpRate counts millionths: 1,000,000 is a rate of 1.0.
RATE_SCALE = 1_000_000
# Rate 0.1: 149 of the 199 fish in the SellingToNpc_Table sheet of a private
# server on client 1784.
RATE_0_1 = 100_000


def sale_exp_at_1000(trade_exp: int, rate: int) -> int:
    """The Trading EXP of one item sold at 1,000 distance, before the EXP multiplier."""
    distance_scaled = max(1, trade_exp)
    return max(1, distance_scaled * rate // RATE_SCALE)
