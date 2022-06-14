def get_input_number(message: str) -> int:
    ret = ''
    while not ret.isdigit():
        ret = input(message)
    return int(ret)


def get_length(sequence: list) -> int:
    return len(sequence)


def get_sum_elements(sequence: list) -> int:
    ret = 0
    for element in sequence:
        ret += element
    return ret


def get_multiplication_elements(sequence: list) -> int:
    ret = 1
    for element in sequence:
        ret *= element
    return ret


def get_arithmetical_mean(sequence: list) -> float:
    try:
        ret = get_sum_elements(sequence) / get_length(sequence)
        ret = ret * 10 // 1 / 10
        return ret
    except ZeroDivisionError:
        print('Ділити на нуль, не можна.')
        return 0


def get_big_number(sequence: list) -> tuple:
    n = 0
    index = 0
    for i, element in enumerate(sequence):
        if n < element:
            n = element
            index = i + 1
    return index, n


def get_amount_even_numbers(sequence: list) -> int:
    count = 0
    for element in sequence:
        if element % 2 == 0:
            count += 1
    return count


def get_amount_odd_numbers(sequence: list) -> int:
    count = 0
    for element in sequence:
        if element % 2 != 0:
            count += 1
    return count


def get_second_big_number(sequence: list, first_big_number: int) -> tuple:
    n = 0
    for element in sequence:
        if n < element < first_big_number:
            n = element
    return n


def get_amount_element_equal_number(sequence: list, number: int) -> int:
    count = 0
    for element in sequence:
        if element == number:
            count += 1
    return count


def main():
    list_number = []
    input_number = ''

    while input_number != 0:
        input_number = get_input_number('Введіть ціле не від`ємне число: ')
        if input_number != 0:
            list_number.append(input_number)

    print(f'Послідовність введених елементів: {list_number}')
    print(f'Кількість елементів: {get_length(list_number)}')
    print(f'Сума елементів: {get_sum_elements(list_number)}')
    print(f'Добуток елементів: {get_multiplication_elements(list_number)}')
    print(f'Середнє арифметичне елементів: {get_arithmetical_mean(list_number)}')
    print(f'Кількість парних елементі: {get_amount_even_numbers(list_number)}')
    print(f'Кількість не парних елементів: {get_amount_odd_numbers(list_number)}')
    big_number = get_big_number(list_number)
    print(f'Найбільший елемент {big_number[1]} за номером {big_number[0]}')
    print(f'Другий найбільший елемент: {get_second_big_number(list_number, big_number[1])}')
    print(f'Кількість найбільших елементів: {get_amount_element_equal_number(list_number, big_number[1])}')


if __name__ == '__main__':
    main()
