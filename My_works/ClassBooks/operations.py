import os

class WorkWithList:

    def __init__(self):
        self.array = []

    def show(self):
        if len(self.array) == 0:
            print("array is empty")
        print('\n', self.array)

    def addEnd(self):
        l = len(self.array)
        if l == 0:
            self.array.append(input("Enter value: "))
        else:
            c = 1
            while c:
                ind = int(input(f"Enter number of array for value (1 - {l+1}): "))
                if ind <= l+1 and ind > 0:
                    val = input("Enter value: ")
                    self.array.insert(ind-1, val)
                    c = not c
                else:
                    print("you enter incorrect index!")

    def dellEnd(self):
        l = len(self.array)
        if l == 0:
            print("array is empty")
        elif l == 1:
            print(f"value {self.array.pop()} deleted")

        else:
            c = 1
            while c:
                ind = int(input(f"Enter number of array for delete value (1 - {l}): "))
                if ind <= l and ind > 0:
                    print(f"value {self.array.pop(ind-1)} deleted")
                    c = not c
                else:
                    print("you enter incorrect index!")

    def sortArr(self):
        self.array.sort()

    def mainMenu(self):
        menu = int(input("\n1 - Show / 2 - Add / 3 - Dell / 4 - Sort / 5 - Exit \nSelect menu item (1-5): "))
        return menu



l = WorkWithList()
run = 1
while run:
    i = l.mainMenu()
    os.system('cls' if os.name == 'nt' else 'clear') # ОЧИЩАЕМ ТЕРМИНАЛ!!!
    if i == 1:
        l.show()
    elif i == 2:
        l.addEnd()
    elif i == 3:
        l.dellEnd()
    elif i == 4:
        l.sortArr()
    elif i == 5:
        run = 0
    else:
        print("error input")
