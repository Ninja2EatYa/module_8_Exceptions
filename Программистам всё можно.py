def add_everything_up(a, b):
    try:
        print('Ура! Условие соблюдено:', round(float(f'{a + b}'), 3))
    except TypeError as exc:
        print(f'Условие - {exc} - не соблюдено: {str(a) + str(b)}')



add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
