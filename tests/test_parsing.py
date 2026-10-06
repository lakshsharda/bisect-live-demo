import pytest

from unitkit.parsing import Quantity, convert_text, parse_quantity


def test_parse_with_space():
    assert parse_quantity("5 km") == Quantity(5.0, "km")


def test_parse_without_space():
    assert parse_quantity("12kg") == Quantity(12.0, "kg")


def test_parse_negative_decimal():
    assert parse_quantity("-3.5 C") == Quantity(-3.5, "C")


def test_parse_garbage():
    with pytest.raises(ValueError, match="cannot parse"):
        parse_quantity("lots of km")


def test_convert_text():
    q = convert_text("1 mi to km")
    assert q.unit == "km" and q.value == pytest.approx(1.609344)


def test_convert_text_needs_to():
    with pytest.raises(ValueError, match="expected the form"):
        convert_text("5 km")
