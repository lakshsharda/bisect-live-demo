import pytest

from unitkit.units import IncompatibleUnits, convert


def test_km_to_m():
    assert convert(2, "km", "m") == pytest.approx(2000)


def test_mile_to_km():
    assert convert(1, "mi", "km") == pytest.approx(1.609344)


def test_pound_to_kg():
    assert convert(10, "lb", "kg") == pytest.approx(4.5359237)


def test_celsius_to_fahrenheit():
    assert convert(100, "C", "F") == pytest.approx(212)


def test_fahrenheit_to_celsius():
    assert convert(-40, "F", "C") == pytest.approx(-40)


def test_absolute_zero_kelvin_to_celsius():
    assert convert(0, "K", "C") == pytest.approx(-273.15)


def test_zero_length_converts_to_zero():
    assert convert(0, "km", "mi") == 0


def test_zero_mass_converts_to_zero():
    assert convert(0, "kg", "lb") == 0


def test_incompatible_kinds():
    with pytest.raises(IncompatibleUnits):
        convert(1, "kg", "m")


def test_below_absolute_zero_rejected():
    with pytest.raises(ValueError):
        convert(-300, "C", "K")


def test_unknown_unit_rejected():
    with pytest.raises(ValueError, match="unknown unit"):
        convert(1, "parsec", "m")
