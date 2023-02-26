class Human:
    def __init__(self, name, age):
        self.__name = name  # объявляем приватный атрибут
        self.age = age

    # def set_name__(self, name):  # сеттер - позволяет изменять приватный атрибут
    #     self.__name = name
    #
    # def get_name__(self):  # геттер - позволяет обращаться (брать) атрибут с приватным модификатором
    #     return self.__name

    #####  МОЖНО с помощью нотаций сделать геттер  и сеттер под одним именем

    @property #  нотация для геттера
    def name(self):
        return self.__name

    @name.setter #  нотация для cеттера
    def name(self, name):
        if 3 < len(name) < 8 : # вводим фильтр\условие или ещё что-н для изменения приватного атрибута
            self.__name = name
            print("обновление атрибута name успешно завершено")
        else:
            print("некорректная длина атрибута!")
    # теперь мы можем обращаться к приватному атрибуту по одному имени

    def __str__(self):
        return f'Всем привет! Меня зовут {self.__name}  и мне {self.age} лет.'

class Worker(Human):
    info = "worker - это класс-дочка от класса Human. в нём будет пример метода класса, который будет показывать вот эту инф-ю о классе, и статический метод, который пока не понятно зачем нужен"
    def __init__(self,  name, age, profession='Unknown', experience='Unknown'):
        super().__init__(name, age)
        self.profession = profession
        self.experience = experience

    @classmethod        # МЕТОД КЛАССА вызывается Worker.show_class_info()
    def show_class_info(cls):
        print(f'about this class: ', cls.info)

    @staticmethod  # ПРИМЕР СТАТИЧЕСКОГО МЕТОДА
    def my_static_method(n):
        print(a)

    def __str__(self):
        return super().__str__() + f'\nЯ работаю {self.profession} уже {self.experience} лет.'

dima = Worker('Dmitry', 18)
dima.name = 'Dima'
print(dima)


a = tuple(map(int, input('введите высоту и ширину книги через пробел в миллиметрах:\n').split()))
print(a[1])