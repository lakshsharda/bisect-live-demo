import pytest

from unitkit.units import convert
from unitkit.validation import validate_magnitude


def test_zero_magnitude_is_allowed():
    """Zero values for non‑temperature kinds should be accepted.

    The original implementation allowed a base value of zero, but the
    simplified validation incorrectly rejects it (``base_value <= 0``).
    This test ensures that converting zero returns zero and that the
    validation function does not raise.
    """
    # Conversion of a zero length should succeed and yield zero.
    assert convert(0, "km", "mi") == 0
    # Direct validation should not raise for zero length.
    validate_magnitude(0.0, "length")
