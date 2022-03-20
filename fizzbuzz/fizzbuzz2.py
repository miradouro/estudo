def robot(num):
    resposta = ""
    if num % 5 == 0 and num % 3 == 0:
        resposta = 'fizzbuzz'
    elif num % 5 == 0:
        resposta = 'buzz'
    elif num % 3 == 0:
        resposta = 'fizz'
    else:
        resposta = str(num)
    return resposta


if __name__ == "__main__":
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'

print(robot(15))
