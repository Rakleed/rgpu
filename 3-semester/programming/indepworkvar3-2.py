"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ВСР 3.2. Задание: реализовать программу шифрующую строку, задава-
    емую пользователем, с помощью алгоритма шифрования, использующего
    сдвиг на определенное количество знаков (шифр Цезаря). Сдвиг
    задается пользователем.

"""


def caesar_cipher(shift, text_to_encrypt):
    cipher_text = ''
    for i in text_to_encrypt:
        if 'a' <= i <= 'z':
            algorithm = chr((ord(i) + shift - ord('a')) % 26 + ord('a'))
            cipher_text += algorithm
        elif 'A' <= i <= 'Z':
            algorithm = chr((ord(i) + shift - ord('A')) % 26 + ord('A'))
            cipher_text += algorithm
        elif 'а' <= i <= 'я':
            algorithm = chr((ord(i) + shift - ord('а')) % 30 + ord('а'))
            cipher_text += algorithm
        elif 'А' <= i <= 'Я':
            algorithm = chr((ord(i) + shift - ord('А')) % 30 + ord('А'))
            cipher_text += algorithm
        else:
            cipher_text += i
    return cipher_text


def main():
    text_to_encrypt = input('Введите строку: ')
    shift = int(input('Введите сдвиг: '))
    print('Получившаяся строка:', caesar_cipher(shift, text_to_encrypt))


main()
