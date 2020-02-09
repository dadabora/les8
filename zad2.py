class Iskl:
    """Класс исключения деления на ноль"""
    def zero_p(self):

        while True:
            try:
                vvod = int(input("Первое число"))
                delitel = int(input("Делитель"))


            except ValueError:
                print("Вводить нужно цифры")
                continue
            try:
                otvet = (vvod/delitel)
            except ZeroDivisionError:
                print("Это выражение деления, деление на ноль не возможно")
                continue
            return otvet
        return






iskl = Iskl()
print(iskl.zero_p())


