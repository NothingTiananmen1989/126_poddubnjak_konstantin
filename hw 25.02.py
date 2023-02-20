import math
print("!!!Обязательно указывайте систему счисления (тонны/кг и км/м)!!!")
def g(weight, distance):
    if weight[-1:] != 'н' and weight[-1:] != 'г' or distance[-2:] != 'км' and distance[-2:] != ' м':       #проверка на правильность написания системы счисления
        print("Ошибка в вводе системы счисления")
        quit()
    if weight[-1:] == 'н':                             #если масса в тоннах, подсчёт и перевод в кг
        weight = str(eval(weight[:-5]) * 1000)
    if weight[-1:] == 'г':                             #если масса в кг, то просто подсчёт
        weight = str(eval(weight[:-3]))

    if distance[-2:] == 'км':                             #если расстояние в километрах, подсчёт и перевод в метры
        distance = str(eval(distance[:-3]) * 1000)
    if distance[-2:] == ' м':                             #если расстояние в метрах, то просто подсчёт
        distance = str(eval(distance[:-2]))


    a = str((6.6743 * math.pow(10, -11) * 5.97600 * math.pow(10, 24) * float(weight)) / math.pow(float(distance), 2))          #подсчёт формулы
    v=0
    for i in range(len((a))):                                    #приведение записи к виду x + 10^N (высчитывание степени  10-ти и округление)
        if a[i] == "e":
            d = a[i+2:]
            c = float(a[:i])
            return("Сила гравитации равна " + str(round(c)) + " x 10^" + str(d) + " H")
    if not("e" in a):
        a=round(float(a))
        if a%10==0:
            while a%10==0:
                a/=10
                v+=1
            return("Сила гравитации равна " + str(round(a)) + " x 10^" + str(v) + " H")
        return("Сила гравитации равна " + str(a) + " Н")

print("Введите массу небесного тела:")
weight=str(input())
print("Введите расстояние до Земли:")
distance=str(input())