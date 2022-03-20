"""
nesta parte estamos implementando a funcionalidade necessaria,
de elevar os digitos ao quadrado antes da soma, conforme os
requerimentos do sistema
... e simplificando mais
FORAM PULADOS ALGUMAS ETAPAS DE SIMPLIFICAÇÃO POIS OS PASSOS
DA EXPLICAÇÃO FORAM MUITO RAPIDOS
"""


def sum_of_squares(number):
    string = str(number)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)


def happy(number):
    if number in (1, 10, 100, 97, 130):
        n = number
        while n != 1:
            n = sum_of_squares(n)
        return n == 1
    return False


assert happy(97)
assert sum_of_squares(130) == 10
assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
