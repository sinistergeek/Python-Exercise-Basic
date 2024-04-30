def comma_fix(data:str) -> float:
    try:
        return float(data)
    except ValueError:
        return float(data.replace(",", ""))

def clean_sum(
        cleaner: Callable[[str],float],
        data: Iterable[str]
    ) -> float:
    return reduce(operator.add,map(cleaner.data))
