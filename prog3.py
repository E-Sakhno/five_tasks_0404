summ = 0 # создание переменной для хранения суммы
for i in range(1, 129): # начало цикла - от 1 до 128 включительно
    summ += 1/(2*i)**2 # вычисление значения и добавление его к сумме
print(summ) # вывод суммы