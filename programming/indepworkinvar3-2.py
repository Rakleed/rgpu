"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 3.2. Задание: создать геттеры и сеттеры для классов «запись»,
    «комментарий» приложения «Гостевая книга», а также функции для
    вывода на печать информации, хранящийся в объектах.

"""


class Post:
    def __init__(self, author, post_text):
        self.__author = author
        self.__post_text = post_text

    def show_comment(self, comment=object):
        print(f'Никнейм: "{comment.nickname}", текст комментария: "{comment.comment_text}".')


class Comment(Post):
    def __init__(self, nickname, comment_text):
        self.__nickname = nickname
        self.__comment_text = comment_text

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def title(self, value):
        self.__nickname = str(value)

    @nickname.deleter
    def title(self):
        self.__nickname = None

    @property
    def comment_text(self):
        return self.__comment_text

    @comment_text.setter
    def comment_text(self, value):
        self.__comment_text = str(value)

    @comment_text.deleter
    def comment_text(self):
        self.__comment_text = None

    def show(self):
        print("Автор: " + str(self.author))
        print("Текст поста: " + str(self.post_text))


post_test = Post("Пётр Михайлов", "Какая-то классная статья.")
comment_test = Comment("alex_356", "Nice!")
post_test.show_comment(comment=comment_test)
