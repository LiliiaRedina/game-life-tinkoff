import time
import copy
import random
import os

def begin(a): #изначальная рандомная генерация океана
    rnd = ['-', '^', 'P', 'K']
    for i in range(n):
        for j in range(n):
            a[i][j] = random.choice(rnd) #рандомный выбор объекта

def upd(a, a1): #изменение поля
    for i in range(n):
        for j in range(n):
        #подсчет соседей-рыб и соседей-креветок для каждой клетки
            p = 0
            k = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (n > i + x >= 0 and n > j + y >= 0) and (x != 0 or y != 0):
                        p += (a[i + x][j + y] == "P")
                        k += (a[i + x][j + y] == "K")
            #изменение океана по правилам
            if (a[i][j] == "P" and (p >= 4 or p < 2)) or (a[i][j] == "K" and (k >= 4 or k < 2)):
                a1[i][j] = "-"
            elif a[i][j] == "-" and p == 3:
                a1[i][j] = "P"
            elif a[i][j] == "-" and k == 3:
                a1[i][j] = "K"

a = []
n = int(input()) #ввод размеров океана
for i in range(n):
    a.append(['-'] * n) #изначальное заполнение пустого океана
begin(a) #изначальная генерация
while True:
    os.system('cls') #очистка экрана
    for i in range(n):
        print(*a[i]) #вывод океана
    time.sleep(4)
    a1 = copy.deepcopy(a) #создание копии для изменения рыб и креветок
    upd(a, a1) #изменение
    a = copy.deepcopy(a1) #перенос изменений на основное поле
