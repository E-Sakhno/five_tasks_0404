K = []  # массив для входных чисел
koef = [1, 4, 7, 10, 13]  # массив коэффициентов
m = 5  # модуль
K_new = []  # массив для выходных чисел

for i in range(6):  # начало цикла
    while True:  # начало бесконечного цикла
        ch = input("Введите " + str(i+1) + "-е число: ")  # запрос ввода числа
        if ch.isnumeric():   # проверка, является ли введенное числом
            if int(ch) < 1000 or int(ch) > 100000:  # если да, то проверка, 4-5-значное ли число
                # если не 4-5-значное, то вывод соответствующего сообщения и возврат в начало цикла
                print("Число не в заданном диапазоне")
            else:  # если 4-5-значное
                K.append(int(ch))  # то добавление числа к массиву
                break  # выход из цикла while
        else:  # если введено не число
            # вывод соответствующего сообщения и возврат в начало цикла
            print("Введено не число, повторите ввод")
print("Входной массив:", K)  # вывод входного массива

for i in range(6):  # для каждого числа
    # рассматриваем число как строку, чтобы можно было пройтись по каждой цифре
    s = str(K[i])
    summ = 0  # переменная для суммы произведений цифр и коэффициентов
    for j in range(1, len(s)+1):  # для каждой цифры
        # умножаем цифру на коэффициент (срез нужен, чтобы правильно определить коэффициенты)
        summ += int(s[j-1])*koef[0:len(s)][-j]
    kontr = summ % m - m  # расчет контрольного числа
    # добавление к выходному массиву контрольного числа и числа из входного массива
    K_new.append(str(kontr)+s)
print("Выходной массив", K_new)  # вывод выходного массива
print("Модуль: ", m)  # вывод модуля
# вывод коэффициентов (если все числа 4-значные, выводится 4 значения)
print("Коэффициенты: ", koef[0:len(str(max(K)))])