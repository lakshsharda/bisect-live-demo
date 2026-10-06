"""Turn numbers and quantities into display strings."""


def format_quantity(value: float, unit: str, precision: int = 2) -> str:
    if precision < 0:
        raise ValueError("precision must be >= 0")
    return f"{value:.{precision}f} {unit}"
