def remove(str: Text, chars: Text) -> Text:
    if chars:
        return remove(str.replace(chars[0], ""),chars[1:])
    return str
