import pytest

from unitkit.formatting import format_quantity


def test_default_precision():
    assert format_quantity(3.14159, "km") == "3.14 km"


def test_zero_precision():
    assert format_quantity(2.5, "kg", precision=0) == "2 kg"


def test_negative_precision_rejected():
    with pytest.raises(ValueError):
        format_quantity(1, "m", precision=-1)


def test_thousands_separator():
    assert format_quantity(1234567.891, "m", thousands=True) == "1,234,567.89 m"


def test_no_thousands_separator_by_default():
    assert format_quantity(1234567.891, "m") == "1234567.89 m"
