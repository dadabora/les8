class Date:
    def __init__(self, d_m_g):
        Date.d_m_g = d_m_g

    @classmethod
    def de_me(cls):
        dmg_n = cls.d_m_g.split('.' or ',' or ' ')
        print(dmg_n)
        dmg_n = [int(el) for el in dmg_n]
        return dmg_n

    @staticmethod
    def val(cls):

        if len(str(a[2])) == 4:
            print(a[2], 'Год норм')
        else:
            print(a[2], 'Год не соответствует')
        if 1 <= a[1] <= 12:
            print(a[1], 'Месяц норм')
            if a[1] == 2:
                if 1 <= a[0] <= 29:
                    print(a[0], 'Число норм')
                else:
                    print(a[0], 'Число не соответствует')
            elif a[1] == 1 or a[1] == 3 or a[1] == 5 or a[1] == 7 or a[1] == 8 or a[1] == 10 or a[1] == 12:
                if 1 <= a[0] <= 31:
                    print(a[0], 'Число норм')
                else:
                    print(a[0], 'Число не соответствует')
            elif a[1] == 4 or a[1] == 6 or a[1] == 9 or a[1] == 11:
                if 1 <= a[0] <= 30:
                    print(a[0], 'Число норм')
                else:
                    print(a[0], 'Число не соответствует')
        else:
            print(a[1], 'Месяц не соответствует')


dey_x = input('Введите датe, в формате дд.мм.гггг-')
date = Date(dey_x)
a = (date.de_me())
print(a[0],'.', a[1],'.', a[2])
date.val(a)