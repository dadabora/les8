class Sklad:
       # внутреннее перемещение
    def peremeschenie(slc, ves_sklad, komy, c, kyda):
        #вынимание оргтехники из списка
        ykogo = ves_sklad.get(komy)
        shto = ykogo.get(c)
        pered = shto.pop(0)
        #перезапись места изъятия
        ykogo.update({c: shto})
        ves_sklad.update({komy: ykogo})
        #перенос изьятой оргтехники
        ykogo = ves_sklad.get(kyda)
        shto = ykogo.get(c)
        shto.append(pered)
        ykogo.update({c: shto})
        ves_sklad.update({kyda: ykogo})
        print('Перемещено  в -  ', kyda, c, shto)
        return ves_sklad




class Org_t:
    # поступление на фирму
    def postupl(slc, ves_sklad, c, inventar_nambe):
        ykogo = ves_sklad.get('склад')
        shto = ykogo.get(c)
        ykogo1 = input('введите модель - ')
        shto1 = {inventar_nambe: ykogo1}
        shto.append(shto1)
        ykogo.update({c: shto})
        ves_sklad.update({'склад': ykogo})
        print('Теперь на складе - ', c, shto)
        return ves_sklad

    def post(slc):
        print('Поступление')

class Pr(Org_t):
    def post(slc):
        print('Поступление принтера')



class Sk(Org_t):
    def post(slc):
        print('Поступление сканера')



class Cs(Org_t):
    def post(slc):
        print('Поступление ксерокса')


class Iskl:
    '''проверка ввода цифр'''

    def zero_p(cls):
        while True:
            try:
                vvod = input(" - ")
                if vvod == 'q':
                    vvod = 4
                    break
                vvod = int(vvod)
                if type(vvod) == int and 1 <= vvod <= 3:
                    break
                else:print('Нет такой команды')
            except ValueError:
                print("Нет такой команды или q")

                continue
        return vvod


a = 0
b = 0
c = 0
vvod = 0
inventar_nambe = 12
ves_sklad = {'склад': {'принтер': [{1: 'модель-1'}], 'сканер': [{2: 'модель-3'}], 'ксерокс': [{3: 'модель-2'}]},
               'отдел продаж': {'принтер': [{5: 'модель-1'}], 'сканер': [{4: 'модель-3'}], 'ксерокс': [{6: 'модель-2'}]},
               'бугалтерия': {'принтер': [{7: 'модель-1'}], 'сканер': [{8: 'модель-3'}], 'ксерокс': [{9: 'модель-2'}]},
               'директор': {'принтер': [{10: 'модель-1'}], 'сканер': [{11: 'модель-3'}], 'ксерокс': [{12: 'модель-2'}]}}

iskl = Iskl()
sklad = Sklad()
org_t = Org_t()

pr = Pr()
sk = Sk()
cs = Cs()

while True:
    print('Для проведения операций введите:\n '
          '1-внутренне перемещение, 2-отчет по складу,'
          ' 3-поступление, q-завершение программы')
    vvod = iskl.zero_p()
    if vvod == 4:
        break
    if vvod == 1:
        try:
            a = int(input('ввести от куда 1-склад, 2-директор, 3-отдел продаж, 4-бугалтерия - '))
        except ValueError:
            print(' нужно вводить цифры')
            continue
        if a == 1:
            komy = 'склад'
            print(komy)
        elif a == 2:
            komy = 'директор'
        elif a == 3:
            komy = 'отдел продаж'
        elif a == 4:
            komy = 'бугалтерия'
        else:
            print('Проверте ввод')
            continue
        try:
            a = int(input('Выберите 1-принтер, 2-сканер, 3-ксерокс - '))
        except ValueError:
            print(' нужно вводить цифры')
            continue
        if a == 1:
            c = 'принтер'
        elif a == 2:
            c = 'сканер'
        elif a == 3:
            c = 'ксерокс'
        else:
            print('Проверте ввод')
            continue
        try:
            a = int(input('Ввести куда 1-склад, 2-директор, 3-отдел продаж, 4-бугалтерия - '))
        except ValueError:
            print(' нужно вводить цифры')
            continue
        if a == 1:
            kyda = 'склад'
            print(kyda)
        elif a == 2:
            kyda = 'директор'
        elif a == 3:
            kyda = 'отдел продаж'
        elif a == 4:
            kyda = 'бугалтерия'
        else:
            print('Проверте ввод')
            continue
        ves_sklad = sklad.peremeschenie(ves_sklad, komy, c, kyda)

        print(ves_sklad)
        continue
    elif vvod == 2:
        print('Наличие по складу - ', ves_sklad.get('склад'))
        print('Наличиче у деректора - ',ves_sklad.get('директор'))
        print('Наличиче у отдела продаж - ',ves_sklad.get('отдел продаж'))
        print('Наличиче у бугалтерии - ',ves_sklad.get('бугалтерия'))
        continue
    elif vvod == 3:
        try:
            a = int(input('Выберите 1-принтер, 2-сканер, 3-ксерокс - '))
        except ValueError:
            print(' нужно вводить цифры')
            continue

        if a == 1:
            c = 'принтер'
            pr.post()
        elif a == 2:
            c = 'сканер'
            sk.post()
        elif a == 3:
            c = 'ксерокс'
            cs.post()
        else:
            print('Проверте ввод')
            continue
        inventar_nambe += 1
        ves_sklad = org_t.postupl(ves_sklad, c, inventar_nambe)