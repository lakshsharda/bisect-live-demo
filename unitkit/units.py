"""Conversion between units of the same kind."""
from .registry import lookup
from .validation import validate_magnitude, validate_unit


class IncompatibleUnits(ValueError):
    """Raised when asked to convert, for example, a length into a mass."""


def to_base(value: float, src: str) -> float:
    unit = lookup(src)
    return value * unit.factor + unit.offset


def from_base(base: float, dst: str) -> float:
    unit = lookup(dst)
    return (base - unit.offset) / unit.factor


def convert(value: float, src: str, dst: str) -> float:
    validate_unit(src)
    validate_unit(dst)
    a, b = lookup(src), lookup(dst)
    if a.kind != b.kind:
        raise IncompatibleUnits(f"cannot convert {a.kind} to {b.kind}")
    base = to_base(value, src)
    validate_magnitude(base, a.kind)
    return from_base(base, dst)
