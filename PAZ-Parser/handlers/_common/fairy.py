"""Fairy grade constants shared by the fairy handlers.

The four fairy grades are keyed by `acquire_type_id` in
`fairyequipskillaquire.dbss`, and by ascending tier everywhere the grade is
implied by position instead of stored (for example the upgrade steps in
`fairyupgraderate.bss`).
"""

from __future__ import annotations


# acquire_type_id -> (tier, grade name), ascending by tier.
FAIRY_GRADES: dict[int, tuple[int, str]] = {
    501: (1, "Faint"),
    502: (2, "Glimmering"),
    503: (3, "Brilliant"),
    504: (4, "Radiant"),
}

# Grade names ordered by tier, so tier N is FAIRY_GRADE_NAMES[N - 1].
FAIRY_GRADE_NAMES: tuple[str, ...] = tuple(
    name for _, name in sorted(FAIRY_GRADES.values())
)

UPGRADE_ARROW = "→"


def upgrade_step_label(step: int) -> str:
    """Return the grade transition label for a zero-based upgrade step.

    Step 0 is the upgrade from the lowest grade to the next one. Returns an
    empty string when the step falls outside the known grade ladder.
    """
    if step < 0 or step + 1 >= len(FAIRY_GRADE_NAMES):
        return ""

    return (
        f"{FAIRY_GRADE_NAMES[step]} {UPGRADE_ARROW} "
        f"{FAIRY_GRADE_NAMES[step + 1]}"
    )
