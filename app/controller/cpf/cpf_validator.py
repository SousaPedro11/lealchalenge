import re


def processa_digitos(string: str) -> str:
    while len(string) < 11:
        soma = sum(int(a) * b for a, b in zip(string, range(len(string) + 1, 1, -1))) % 11
        digito = 0 if soma < 2 else 11 - soma
        string += str(digito)
    print(string)
    return string


def validar(entrada: str) -> bool:
    entrada = ''.join(re.findall('\\d+', entrada))

    if len(entrada) != 11:
        return False

    for i in range(10):
        if entrada.count(str(i)) == 11:
            return False

    print(entrada)
    return entrada == processa_digitos(entrada[:9])
