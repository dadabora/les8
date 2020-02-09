class Comp_namb:
    def razl(cls, z1, z2):
        #разделение на составляющие
        zet1 = z1.split(' ')
        #разделение на состовляющее числа с i
        zei1 = zet1[2].split('*')
        #предворительное вычисление числа с i для сложения
        zet2 = z2.split(' ')
        zei2 = zet2[2].split('*')
        z1a = zet1[0]
        z2a = zet2[0]
        z1b = str(zet1[1]) + str(zei1[0])
        z2b = str(zet2[1]) + str(zei2[0])
        #предворительное вычисление числа с i для умножения
        z3b = int(z1b) + int(z2b)
        z4b = (int(z1b) * int(z2b)) + (int(z1b) * int(z2a)) + (int(z1a) * int(z2b))
        # проверка полученного значения числа с i для подстановки символа
        if z3b >= 0:
            t = ' + '
        elif z3b < 0:
            t = ' - '

        if z4b > 0:
            m = ' + '
        elif z4b < 0:
            m = ' - '
        # сбор в единую строку двух вариантов вычислений
        z3 = (str(int(z1a) + int(z2a)) + t + str(z3b) + '*i')
        z4 = (str(int(z1a) * int(z2a)) + m + str(z4b) + '*i')
        print(z3)
        print(z4)
        return z3, z4


z1 = '10 + 4*i'
z2 = '15 - 3*i'
print("z1 = " + z1)
print("z2 = " + z2)
slog = Comp_namb()
z3, z4 = slog.razl(z1, z2)
print('Итого сложение комплексных чисeл z1+z2 = ' + z3)
print('Итого произведение комплексных чисeл z1*z2 = ' + z4)