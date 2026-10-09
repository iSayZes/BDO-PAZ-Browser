"""Effect text and Param column labels from a buff's parameters."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from .formats import EFFECT_LINES, FIXED_TEXTS, OVER_TIME_EFFECTS, EffectLine, OverTimeEffect
from .named import NAMED_EFFECTS, NamedEffect
from .units import format_amount, seconds_text

# Named templates may hold `{param_1}` to `{param_10}`.
_PARAM_COUNT = 10


@dataclass(frozen=True)
class EffectInput:
    """The buff fields an effect reads.

    `params` holds `param_1` onwards, so `params[0]` is `param_1`. The other
    fields are read by types 1 and 4 only.
    """

    effect_type: int
    params: Sequence[int]
    tick_ms: int = 0
    condition_type: int = 0
    duration_ms: int = 0
    icon_path: str = ""

    def param(self, number: int) -> int:
        """`param_<number>`, or 0 past the end of `params`."""
        return self.params[number - 1] if number <= len(self.params) else 0


def _holds(when: Mapping[int, int], buff: EffectInput) -> bool:
    return all(buff.param(number) == kind for number, kind in when.items())


def _applies(line: EffectLine, buff: EffectInput) -> bool:
    return buff.param(line.value_param) != 0 and _holds(line.when, buff)


def _applying_lines(buff: EffectInput) -> list[EffectLine]:
    return [line for line in EFFECT_LINES.get(buff.effect_type, ()) if _applies(line, buff)]


def _kind_name(line: EffectLine, buff: EffectInput) -> str:
    """The LOC name of the line's kind (`Hunting`), '' for a fixed label."""
    return line.kind_name(buff.param(line.kind_param)) if line.kind_name else ""


def _line_label(line: EffectLine, buff: EffectInput) -> str:
    return line.label.format(kind=_kind_name(line, buff)) if line.kind_name else line.label


def _line_text(line: EffectLine, buff: EffectInput) -> str:
    value = buff.param(line.value_param)
    amount = format_amount(-value if line.is_negated else value, line.unit, signed=line.is_signed)
    return line.template.format(label=_line_label(line, buff), amount=amount)


def _line_labels(line: EffectLine, buff: EffectInput) -> dict[int, str]:
    labels = dict(line.kind_labels)
    if line.kind_name:
        labels[line.kind_param] = _kind_name(line, buff)
    if line.value_label:
        labels[line.value_param] = line.value_label
    elif line.unit.is_scaled:
        labels[line.value_param] = format_amount(buff.param(line.value_param), line.unit, signed=False)
    return labels


def _named_effect(buff: EffectInput) -> NamedEffect | None:
    """The first named entry of the buff's type whose `when` holds."""
    return next((e for e in NAMED_EFFECTS.get(buff.effect_type, ()) if _holds(e.when, buff)), None)


def _named_key(effect: NamedEffect, buff: EffectInput) -> tuple[list[int], str]:
    """The key values and their LOC name, '' when LOC has none."""
    key = [buff.param(number) for number in effect.key_params]
    return key, effect.name_of(*key)


def _named_text(effect: NamedEffect, buff: EffectInput) -> str:
    """`Summon Rock Golem`, or the key when LOC has no name for it."""
    key, name = _named_key(effect, buff)
    if not name and not effect.is_key_shown:
        return ""
    key_text = "/".join(str(value) for value in key)
    params = {f"param_{number}": buff.param(number) for number in range(1, _PARAM_COUNT + 1)}
    if name:
        return effect.template.format(name=name, key=key_text, **params)
    return (effect.unnamed_template or effect.template).format(name=key_text, key=key_text, **params)


def _over_time_trigger(effect: OverTimeEffect, buff: EffectInput) -> str:
    """`on Hits`, `when struck` or `every 10 sec`; '' when no text applies.

    Without a tick or a known condition there is none: a one-off amount that
    type 4 also uses for a mount's stamina (carrots).
    """
    amount = buff.param(1)
    if amount == 0:
        return ""
    if buff.condition_type != 0:
        if amount > 0:
            return effect.recover_on.get(buff.condition_type, "")
        fixed = effect.fixed_damage_on.get(buff.condition_type)
        return fixed.trigger if fixed else ""
    return f"every {seconds_text(buff.tick_ms)} sec" if buff.tick_ms > 0 else ""


def _over_time_text(effect: OverTimeEffect, buff: EffectInput) -> str:
    """`Recover 250 MP/WP/SP every 10 sec`, `200 poison damage every 2 sec for 10 sec`."""
    trigger = _over_time_trigger(effect, buff)
    if not trigger:
        return ""
    amount = buff.param(1)
    if amount > 0:
        return f"Recover {amount:,} {effect.resource} {trigger}"
    fixed = effect.fixed_damage_on.get(buff.condition_type)
    if fixed is not None:
        return f"{fixed.verb} {-amount:,} Fixed Damage {trigger}"
    kind = effect.damage_kinds.get(buff.icon_path.rsplit("/", 1)[-1])
    if kind is None:
        return f"{effect.resource} {amount:,} {trigger}"
    lasting = f" for {seconds_text(buff.duration_ms)} sec" if buff.duration_ms > 0 else ""
    return f"{-amount:,} {kind} damage {trigger}{lasting}"


def effect_text(buff: EffectInput) -> str:
    """`All AP +8` for a confirmed effect type, else ''. A zero amount yields '' too."""
    fixed = FIXED_TEXTS.get(buff.effect_type)
    if fixed is not None:
        return fixed
    over_time = OVER_TIME_EFFECTS.get(buff.effect_type)
    if over_time is not None:
        return _over_time_text(over_time, buff)
    if buff.effect_type in NAMED_EFFECTS:
        named = _named_effect(buff)
        return _named_text(named, buff) if named is not None else ""
    return ", ".join(_line_text(line, buff) for line in _applying_lines(buff))


def param_labels(buff: EffectInput) -> dict[int, str]:
    """What each confirmed parameter means, by parameter number.

    `{1: "Kamasylvian Monsters"}`, `{1: "10%"}`, `{1: "Monster AP"}` or
    `{1: "every 10 sec"}`; parameters without a confirmed meaning are left
    out, and so is everything when no text applies.
    """
    over_time = OVER_TIME_EFFECTS.get(buff.effect_type)
    if over_time is not None:
        trigger = _over_time_trigger(over_time, buff)
        return {1: trigger} if trigger else {}
    if buff.effect_type in NAMED_EFFECTS:
        named = _named_effect(buff)
        if named is None:
            return {}
        _, name = _named_key(named, buff)
        return {named.key_params[-1]: name} if name else {}
    labels: dict[int, str] = {}
    for line in _applying_lines(buff):
        labels.update(_line_labels(line, buff))
    return labels
