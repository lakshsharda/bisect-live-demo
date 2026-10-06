import pytest
from unitkit.validation import validate_magnitude

def test_zero_magnitude_is_valid_for_length_mass_and_temperature():
    """Zero values should be accepted for all kinds.

    The original implementation allowed zero for length, mass, and temperature (absolute zero).
    The simplified validation incorrectly rejects zero for every kind, causing conversions like
    ``convert(0, "K", "C")`` or ``convert(0, "km", "mi")`` to raise ``ValueError``.
    This test ensures the regression is caught.
    """
    for kind in ("length", "mass", "temperature"):
        # No exception should be raised for a zero base value.
        validate_magnitude(0.0, kind)
