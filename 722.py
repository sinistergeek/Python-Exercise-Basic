from typing import Optional, Text
def float_none(data: Optional[Text]) -> Optional[float]:
    try:
        data_f = float(data)
        return data_f
    except ValueError:
        return None

