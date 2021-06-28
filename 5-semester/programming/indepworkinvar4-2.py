"""
    Автор: Моисеенко Павел, подгруппа № 2.
    ИСР 4.2. Задание: разработать фрагмент программы с использованием
    библиотеки pyqrcode, позволяющей создавать изображение QR-кода на
    основе переданной в программу текстовой строки.

"""


import pyqrcode


image = pyqrcode.create(input("Введите текст: "))
image.svg("qr.svg")