"""Turn numbers and quantities into display strings."""


def format_quantity(value: float, unit: str, precision: int = 2, thousands: bool = False) -> str:
    if precision < 0:
        raise ValueError("precision must be >= 0")
    sep = "," if thousands else ""
    return f"{value:{sep}.{precision}f} {unit}"
