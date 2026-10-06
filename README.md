# unitkit

Small unit-conversion library for length, mass and temperature.

```python
from unitkit import convert, convert_text
convert(1, "mi", "km")        # 1.609344
convert_text("100 C to F")    # Quantity(value=212.0, unit='F')
```

## Supported units

| Kind | Units |
|---|---|
| Length | m, km, cm, mi, ft |
| Mass | kg, g, lb, oz |
| Temperature | K, C, F |

Long names such as `mile`, `pound` and `celsius` are accepted as aliases.
