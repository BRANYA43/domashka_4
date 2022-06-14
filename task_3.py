from task_1 import get_input_number


def get_sequence_numbers(some_list: list, a: int, b: int):
    while a < b or a > b:
        if a < b:
            some_list.append(a)
            a += 1
        else:
            some_list.append(a)
            a -= 1
    some_list.append(b)


def main():
    sequence_numbers = []
    A = get_input_number(f'Введіть число А: ')
    B = get_input_number(f'Введіть число В: ')
    get_sequence_numbers(sequence_numbers, A, B)
    print(sequence_numbers)


if __name__ == '__main__':
    main()
