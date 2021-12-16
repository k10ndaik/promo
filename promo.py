def calculate(m: int, n: int, p: list=[int]):
#функция подсчета максимальных бонусов
    rez = p.pop(0)
#первый бонус как старт акци пинимается любой
    for x in p:
        if x > n:
            rez += x
#добавляем бонус нажатия если он больше стартого бонуса
        else:
            rez += n
#или стартовый если он больше заданного

    print(rez)
    return rez


def test(rez, rez_bonus):
    if rez == rez_bonus:
        print('все верно')
    else:
        print('не верно')


test(12, calculate(3,3,p=[6, 2, 3]))