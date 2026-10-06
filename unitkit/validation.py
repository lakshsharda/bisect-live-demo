"""Input checks. They raise ValueError with a message that says what is wrong."""
from .registry import lookup


def validate_unit(name: str) -> None:
    if lookup(name) is None:
        raise ValueError(f"unknown unit: {name!r}")


def validate_magnitude(base_value: float, kind: str) -> None:
    """`base_value` is already in the base unit (m, kg or K), so zero is the smallest allowed value."""
    if kind == "temperature":
        if base_value < 0:
            raise ValueError("temperature is below absolute zero")
    else:
        if base_value < 0:
            raise ValueError(f"{kind} cannot be negative")
