"""
    ## Описание задачи
    Написать функцию `squareSequenceDigit()`, где решалась бы
    следующая задача. Найти n-ю цифру последовательности из квадратов
    целых чисел: `149162536496481100121144...`

    Например, 2-я цифра равна 4, 7-я 5, 12-я 6. Использовать операции
    со строками в этой задаче запрещается.

    Протестировать выполнение программы со следующими значениями:
    * при вызове squareSequenceDigit(1) должно быть 1;
    * squareSequenceDigit(2) вернёт 4;
    * squareSequenceDigit(7) вернёт 5;
    * squareSequenceDigit(12) вернёт 6;
    * squareSequenceDigit(17) вернёт 0;
    * squareSequenceDigit(27) вернёт 9.

"""

import math


def count_digit_in_num(number_q):
    digit_size = 0
    while number_q > 0:
        number_q = math.floor(number_q / 10)
        digit_size += 1

    return digit_size


def square_sequence_digit(n):
    number = 1
    digit = 1
    order_digit = 1
    while order_digit <= n:
        number += 1
        number_q = number ** 2
        count_digit = count_digit_in_num(number_q)
        if order_digit + count_digit >= n:
            while order_digit != n:
                count_digit -= 1
                order_digit += 1
                digit = math.floor(number_q / (10 ** count_digit))

        order_digit += count_digit
        digit %= 10

    return digit


if __name__ == "__lab1__":
    square_sequence_digit(1)
    square_sequence_digit(2)
    square_sequence_digit(7)
    square_sequence_digit(12)
    square_sequence_digit(17)
    square_sequence_digit(27)
