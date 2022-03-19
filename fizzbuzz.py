def fizbuzzer(number):
    i = 1
    while i <= number:
        if (i % 3) == 0 and (i % 5) == 0:
            print('fizzbuzz')
            i += 1
        elif (i % 3) == 0:
            print('fizz')
            i += 1
        elif (i % 5) == 0:
            print('buzz')
            i += 1
        else:
            print(i)
            i += 1


fizbuzzer(44)
