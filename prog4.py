import random
n = int(input("Введите размерность матрицы: ")) # запрос размера матрицы
m = [[random.randint(0, 10) for i in range(n)] for j in range(n)] # создание рандомной квадратной матрицы

m_n = [[0 for i in range(n)] for i in range(n)] # создание промежуточной матрицы
m_new = [[0 for i in range(n)] for i in range(n)] # создание пустой матрицы для результата возведения в степень

print('Первоначальная матрица А:') # вывод матрицы
for r in m: 
    print(r)


for i in range(n): 
    for j in range(n): 
        for k in range(n): 
            m_n[i][j] += m[i][k] * m[k][j] # вычисление матрицы в квадрате и запись результата в промежуточную матрицу

for i in range(n): 
    for j in range(n): 
        for k in range(n): 
            m_new[i][j] += m[i][k] * m_n[k][j] # вычисление матрицы в кубе и запись результата в окончательную матрицу

print("A^3:") # вывод матрицы
for r in m_new: 
    print(r)