"""Cell text of the server option tables (`server_tables.py`)."""

from __future__ import annotations


def light_user_reward_text(rewards: list[list[int]]) -> str:
    """The filled `disconnected_time: bonus` entries of a light user bonus row; empty when none is."""
    return ", ".join(f"{time}: {bonus}" for time, bonus in rewards if time or bonus)
