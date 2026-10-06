"""Parse text such as '5 km' or '-3.2 C' and convert it with 'to'."""
import re
from dataclasses import dataclass

from .units import convert

_QUANTITY = re.compile(r"^\s*(-?\d+(?:\.\d+)?)\s*([A-Za-z]+)\s*$")


@dataclass(frozen=True)
class Quantity:
    value: float
    unit: str


def parse_quantity(text: str) -> Quantity:
    m = _QUANTITY.match(text)
    if not m:
        raise ValueError(f"cannot parse quantity: {text!r}")
    return Quantity(float(m.group(1)), m.group(2))


def convert_text(text: str) -> Quantity:
    """'5 km to mi' -> Quantity(3.106..., 'mi')."""
    left, sep, right = text.partition(" to ")
    if not sep:
        raise ValueError("expected the form '<value> <unit> to <unit>'")
    q = parse_quantity(left)
    dst = right.strip()
    return Quantity(convert(q.value, q.unit, dst), dst)
