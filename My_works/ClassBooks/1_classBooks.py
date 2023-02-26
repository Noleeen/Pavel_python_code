class Books:
    def __init__(self, id_num, name, author, amountPages, yearOfWriting, isbn="0"):
        self.__id_num = id_num
        self.name = name
        self.author = author
        self.__amountPages = amountPages
        self.yearOfWriting = yearOfWriting
        self.__isbn = isbn
        self.type = ""

    def typeOfAmountPage(self):
        if self.__amountPages <= 4:
            self.type = "буклет"
        elif 4 < self.__amountPages <= 48:
            self.type = "брошюра"
        elif 48 < self.__amountPages:
            self.type = "книга"

    @property
    def id_num(self):
        return self.__id_num

    @id_num.setter
    def id_num(self, id_num):
        if type(id_num) == int:
            self.__id_num = id_num
        else:
            print("ошибка, введите натуральное число")


    @property
    def amountPages(self):
        return self.__amountPages

    @amountPages.setter
    def amountPages(self, amountPages):
        if type(amountPages) == int:
            self.__amountPages = amountPages
        else:
            print("ошибка, введите натуральное число")


    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        if 13 <= len(isbn) <= 17:
            self.__isbn = isbn
        else:
            print("неверный формат ISBN")

    def __str__(self):
        return f'\n{self.type} {self.name}.\n Автор: {self.author}.\n {self.__amountPages}стр. Написана в {self.yearOfWriting}году. ISBN: {self.__isbn} '


class PaperBooks(Books):
    def __init__(self, id_num, name, author, amountPages, yearOfWriting, isbn, ageBook, typeOfCover=0):
        super().__init__(id_num, name, author, amountPages, yearOfWriting, isbn,)
        self.__typeOfCover = typeOfCover
        self.ageBook = ageBook
        self.cover = ""


    def antique(self):
        if self.ageBook < 70:
            print("Букинистическое издание")
        elif 70 <= self.ageBook < 470:
            print("Антикварная книга")
        elif 470 <= self.ageBook < 520:
            print("Палеотип")
        elif 520 <= self.ageBook < 590:
            print("Инкунабула")
        elif self.ageBook > 590:
            print("Древняя книга")

    def typeCover(self):
        if self.__typeOfCover == 1:
            self.cover = "твёрдая обложка"
        elif self.__typeOfCover == 2:
            self.cover = "мягкая обложка"
        elif self.__typeOfCover == 0:
            self.cover = "тип обложки неопределён"


class ElectronicBooks(Books):
    def __init__(self, id_num, name, author, amountPages, yearOfWriting, isbn, extension='-'):
        super().__init__(id_num, name, author, amountPages, yearOfWriting, isbn,)
        self.extension = extension

    def __str__(self):
        return super().__str__() + f'\n Электронная книга с расширением {self.extension}\n------------------\n'


class Format(PaperBooks):
    def __init__(self, id_num, name, author, amountPages, yearOfWriting, ageBook, cover, isbn="0"):
        super().__init__(id_num, name, author, amountPages, yearOfWriting, isbn, ageBook, cover)
        super().typeCover()
        self.format = ""
        self.format_millimeters = ()


    def inputFormat(self):
        self.format_millimeters = tuple(map(int, input(f'книга {self.name} {self.author} \nвведите меньшую сторону и большую сторону книги через пробел в миллиметрах:\n').split()))

    def formatBooks (self):
        if self.format_millimeters[0] < 76:
            self.format = "Миниатюрные издания"
            print(self.format)
        elif 77 <= self.format_millimeters[0] < 119:
            self.format = "Издания малоформатные"
            print(self.format)
        elif 120 <= self.format_millimeters[0] < 170:
            self.format = "Издания среднего формата"
            print(self.format)
        elif 171 <= self.format_millimeters[0]:
            self.format = "Издания большого формата"
            print(self.format)

    def __str__(self):
        return super().__str__() + f'\n Тип обложки: {self.cover}.\n{self.format}\n------------------\n'

print()
a = Format(1,"Катехизис", "Сымон Будный", " - ", 1562, 461, 1)
a.antique()
print(a)

b = Format(2, "Стихотворения", "Иосиф Бродский", 1016, " - ", 10, 1, "978-5-389-09389-8")
b.antique()
b.inputFormat()
b.formatBooks()
print(b)

c = ElectronicBooks(3, "Код", "Чарльз Петцольд", 444, 1999, " - ", ".pdf")
print(c)


