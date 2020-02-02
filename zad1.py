class Date:
    def __init__(self, d_m_g):
        self.d_m_g = d_m_g

   # @classmethod
    def de_me(self):
        dmg_n = self.d_m_g.split('.')
        dmg_n = [int(el) for el in dmg_n]
        return dmg_n
"""
    def __int__(self, dmg_n):
        self.dmg_n = dmg_n

    @staticmethod
    def val(self):
        print(dmg_n)
        a = self.dmg_n

        if len(a[2]) == 4:
            print(a[2], 'Год норм')
        else:
            print(a[2], 'Не соответствует')

        if 1 <= a[1] <= 12:
            print(a[1], 'Месяц норм')
            if a[1] == 2:
                if 1 <= a[0] <= 29:
                    print(a[0], 'Число норм')
                else:
                    print(a[0], 'Число не соответствует')

            if  a[1] == 1 or a[1] == 3 or a[1] == 5 or a[1] == 7 or a[1] == 8 or a[1] == 10 or a[1] == 12:
                    if 1 <= a[0] <= 31:
                        print(a[0], 'Число норм')
                    else:
                        print(a[0], 'Число не соответствует')

            if  a[1] == 4 or a[1] == 6 or a[1] == 9 or a[1] == 11:
                    if 1 <= a[0] <= 30:
                        print(a[0], 'Число норм')
                    else:
                        print(a[0], 'Число не соответствует')
"""




date = Date("12.04.1960")
print(date.de_me())
#print(date.val(date.de_me()))