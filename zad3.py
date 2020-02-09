class Iskl:

    def zero_p(cls):

        while True:
            try:
                vvod = input("Для окончания команда stop  \n Ввод чисел - ")
                if vvod == 'stop':
                    break
                vvod = int(vvod)
            except ValueError:
                print("Вводить нужно цифры")
                continue
            otvet.append(vvod)
        return otvet




otvet = []

iskl = Iskl()
print(iskl.zero_p())