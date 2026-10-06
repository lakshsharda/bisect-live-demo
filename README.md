# unitkit

Small unit-conversion library for length, mass and temperature.

```python
from unitkit import convert, convert_text
convert(1, "mi", "km")        # 1.609344
convert_text("100 C to F")    # Quantity(value=212.0, unit='F')
```
