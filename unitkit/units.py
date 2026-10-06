"""Conversion between units of the same kind."""
from .registry import lookup
from .validation import validate_magnitude, validate_unit


class IncompatibleUnits(ValueError):
    """Raised when asked to convert, for example, a length into a mass."""


def to_base(value: float, from_unit: str) -> float:
    unit = lookup(from_unit)
    return value * unit.factor + unit.offset


def from_base(base: float, to_unit: str) -> float:
    unit = lookup(to_unit)
    return (base - unit.offset) / unit.factor


def convert(value: float, from_unit: str, to_unit: str) -> float:
    validate_unit(from_unit)
    validate_unit(to_unit)
    a, b = lookup(from_unit), lookup(to_unit)
    if a.kind != b.kind:
        raise IncompatibleUnits(f"cannot convert {a.kind} to {b.kind}")
    base = to_base(value, from_unit)
    validate_magnitude(base, a.kind)
    return from_base(base, to_unit)
