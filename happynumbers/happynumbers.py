"""
neste começo, estamos apenas criando um codigo para somar as
unidades de um numero e verificar se essa somatoria é igual
a zero
"""


def happy(number):
    if number in (1, 10, 100):
        string = str(number)
        """
        # primeira forma
        total, i = 0, 0
        while i < len(string):
            total += int(string[i])
            i += 1
        return total == 1"""

        """
        # segunda forma
        total = 0
        for char in string:
            total += int(char)
        return total == 1"""

        # terceira forma / a evolução
        digits = []
        total = 0
        for char in string:
            digits.append(int(char))
        for digit in digits:
            total += digit
        return total == 1



    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)
