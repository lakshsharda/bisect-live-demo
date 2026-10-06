"""Input checks. They raise ValueError with a message that says what is wrong."""
from .registry import get_unit


def validate_unit(name: str) -> None:
    get_unit(name)  # raises ValueError for an unknown unit


def validate_magnitude(base_value: float, kind: str) -> None:
    """`base_value` is already in the base unit (m, kg or K), so zero is the smallest allowed value."""
    if kind == "temperature":
        if base_value < 0:
            raise ValueError("temperature is below absolute zero")
    else:
        if base_value < 0:
            raise ValueError(f"{kind} cannot be negative")
