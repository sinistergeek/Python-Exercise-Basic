def drop_punct2(text:str) -> str:
    return text.replace(",","").replace("$","")
@cleanse_before(drop_punct)
def to_int(text:str,base:int=10) -> int:
    return int(text,base)
