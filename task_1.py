def get_input_number(message: str) -> int:
    ret = ''
    while not ret.isdigit():
        ret = input(message)
    return int(ret)


def main():
    INCREASE = 1.1
    count_day = 0
    distance = get_input_number('Введіть число скільки пробіг в перший день спортсмен (км): ')
    search_distance = get_input_number('Введіть число скільки повинен пробігти спортсмен (км): ')

    while distance < search_distance:
        distance *= INCREASE
        count_day += 1

    print(f'Спортсмен досяг відмітки {search_distance}(км) у {count_day + 1} день.')


if __name__ == '__main__':
    main()