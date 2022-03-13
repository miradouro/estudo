"""print("Ola,mundo!")"""


"""def donuts(count):
    cont = count
    return print(f'Number of donuts: {count}' if int(count) <= 10 else 'Number of donuts: many')

donuts(11)"""

"""def both_ends(s):
    # +++ SUA SOLUÇÃO +++
    return print(s[:2]+s[-2]+s[-1] if len(s) > 2 else [])

both_ends("string")
"""


"""def fix_start(s):
    # +++ SUA SOLUÇÃO +++
    i = s[0]+s[1:].replace(s[0], "*")
    return print(i)


fix_start("bubble")"""


def not_bad(s):
    # +++ SUA SOLUÇÃO +++
    x = s if 'not' not in s or 'bad' not in s else ""
    y = s.split()
    print(y)

    return x


not_bad('This movie is not so bad')