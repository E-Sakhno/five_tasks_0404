import random
n = int(input("Введите размер массива: ")) # запрос размера массива
m = [random.randint(0, 10) for i in range(n)] # рандом значений
print(m) # вывод начального массива
m.insert(0, m[-1]) # добавление в начало массива элемента, равного последнему
m.pop() # удаление последнего элемента
print(m) # вывод нового массива
