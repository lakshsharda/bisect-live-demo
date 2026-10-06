from unitkit.registry import UNITS, lookup


def test_lookup_known_unit():
    assert lookup("km").factor == 1000.0


def test_lookup_alias():
    assert lookup("mile") is UNITS["mi"]
    assert lookup("Celsius") is UNITS["C"]


def test_lookup_unknown_is_none():
    assert lookup("parsec") is None


def test_every_unit_has_a_known_kind():
    assert {u.kind for u in UNITS.values()} == {"length", "mass", "temperature"}
