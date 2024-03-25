from decimal import *
from typing import Text, Optional
def clean_decimal(text: Text) -> Optional[Text]:
    if text is None: return None
    return Decimal(text.replace("$", "").replace(",", ""))

def replace(str: Text, a:Text,b:Text) -> Text:
    return str.replace(a,b)
