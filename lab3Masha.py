# Домашнее задание 3, вариант 2 (Дата)
class Date:
    day = 0
    month = 0
    year = 0

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def inputStream(self):
        self.day = input()
        self.month = input()
        self.year = input()

    def outputStream(self):
        print(self.day + "." + self.month+"." + self.year)
