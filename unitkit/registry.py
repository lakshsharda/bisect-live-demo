"""The table of known units. Every unit converts to a base unit: metre, kilogram or kelvin."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Unit:
    name: str
    kind: str  # "length" | "mass" | "temperature"
    factor: float  # base = value * factor + offset
    offset: float = 0.0


UNITS: dict[str, Unit] = {
    "m": Unit("m", "length", 1.0),
    "km": Unit("km", "length", 1000.0),
    "cm": Unit("cm", "length", 0.01),
    "mi": Unit("mi", "length", 1609.344),
    "ft": Unit("ft", "length", 0.3048),
    "kg": Unit("kg", "mass", 1.0),
    "g": Unit("g", "mass", 0.001),
    "lb": Unit("lb", "mass", 0.45359237),
    "oz": Unit("oz", "mass", 0.028349523125),
    "K": Unit("K", "temperature", 1.0),
    "C": Unit("C", "temperature", 1.0, 273.15),
    "F": Unit("F", "temperature", 5 / 9, 273.15 - 32 * 5 / 9),
}

ALIASES = {"meter": "m", "metre": "m", "kilometer": "km", "mile": "mi", "foot": "ft", "pound": "lb", "kilogram": "kg",
           "gram": "g", "celsius": "C", "fahrenheit": "F", "kelvin": "K"}  # fmt: skip


def lookup(name: str) -> Unit | None:
    key = ALIASES.get(name.strip().lower(), name.strip())
    return UNITS.get(key)


def get_unit(name: str) -> Unit:
    """Like lookup(), but raises ValueError for an unknown unit."""
    unit = lookup(name)
    if unit is None:
        raise ValueError(f"unknown unit: {name!r}")
    return unit
