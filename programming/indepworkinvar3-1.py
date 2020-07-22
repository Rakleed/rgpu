"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 3.1. Задание: разработать классы и объекты «запись»,
    «комментарий» для приложения «Блог» (использую наследование).

"""


class Post:
    def __init__(self, author, post_text):
        self.__author = author
        self.__post_text = post_text

    def show_comment(self, comment=object):
        print(f'Никнейм: "{comment.nickname}", текст комментария: "{comment.comment_text}".')


class Comment(Post):
    def __init__(self, nickname, comment_text):
        self.nickname = nickname
        self.comment_text = comment_text


post_test = Post("Иван Александров", "Какая-то интересная статья.")
comment_test = Comment("var_inb2", "Great job!")
post_test.show_comment(comment=comment_test)
