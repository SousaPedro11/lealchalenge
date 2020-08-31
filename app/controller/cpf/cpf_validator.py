import re


def processa_digitos(string: str) -> bool:
    base = string[:9]
    while len(base) < 11:
        soma = sum(int(a) * b for a, b in zip(base, range(len(base) + 1, 1, -1))) % 11
        digito = 0 if soma < 2 else 11 - soma
        base += str(digito)

        if string[len(base)-1] != base[len(base)-1]:
            return False

    return True


def validar(entrada: str) -> bool:
    entrada = ''.join(re.findall('\\d+', entrada))

    if len(entrada) != 11:
        return False

    for i in range(10):
        if entrada.count(str(i)) == 11:
            return False

    return processa_digitos(entrada)
