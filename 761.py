from typing import Tuple
def clean_list(text:str,char_list:Tuple[str,...]) -> str:
    if char_list:
        return clean_list(
            text.replace(char_list[0],""),char_list[1:]
        )
    return text
