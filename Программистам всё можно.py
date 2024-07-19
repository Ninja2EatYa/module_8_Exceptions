def add_everything_up(a, b):
    return f'{str(a) + str(b)}' if isinstance(a, str) or isinstance(b, str) else round(float(f'{a + b}'), 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))