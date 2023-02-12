class Books:
    def __init__(self,name,age,amountPages, genre ):
        self.typeOfCover = None
        self.name = name
        self.age = age
        self.genre = genre
        self.amountPages = amountPages

    def antique(self):
        if self.age < 70 :
            print("Букинистическое издание")
        elif 70 <= self.age < 470:
            print("Антикварная книга")
        elif 470 <= self.age < 520:
            print("Палеотип")
        elif 520 <= self.age < 590:
            print("Инкунабула")
        elif self.age > 590:
            print("Древняя книга")

    def typeOfAmountPage(self):
        if self.amount <= 4:
            return "буклет"
        elif 4 < self.amount <= 48:
            return "брошюра"
        elif 48 < self.amount:
            return "книга"

    def typeCover(self, type):
        if type == 1:
            self.typeOfCover = "твёрдая обложка"
        elif type == 2:
            self.typeOfCover = "мягкая обложка"

    def bookInfo(self):
        print(f'Наименование книги: {self.name} \n'
              f'Возраст книги: {self.age}\n'
              f'Количество страниц: {self.amountPages}\n'
              f'Тип обложки: {self.typeOfCover}\n'
              f'Жанр: {self.genre}')