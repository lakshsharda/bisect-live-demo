import pytest

from unitkit.validation import validate_magnitude, validate_unit


def test_known_unit_passes():
    validate_unit("kg")


def test_unknown_unit_rejected():
    with pytest.raises(ValueError, match="unknown unit"):
        validate_unit("parsec")


def test_zero_length_is_valid():
    validate_magnitude(0.0, "length")


def test_zero_mass_is_valid():
    validate_magnitude(0.0, "mass")


def test_absolute_zero_is_valid():
    validate_magnitude(0.0, "temperature")


def test_negative_length_rejected():
    with pytest.raises(ValueError, match="cannot be negative"):
        validate_magnitude(-1.0, "length")


def test_below_absolute_zero_rejected():
    with pytest.raises(ValueError, match="absolute zero"):
        validate_magnitude(-0.5, "temperature")
