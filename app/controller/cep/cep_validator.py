import re


def validar(string: str) -> str:
    return ''.join(list(x for x in string if x.isnumeric())[::-1])


def validar_regex(string: str) -> str:
    return ''.join(re.findall('\\d+', string))[::-1]
