import re

text = 'home sweet , home'
text = re.sub(r'[.,!?:;-]', '', text)
words = text.split()

# Расчет n строки треугольника Паскаля
def pascal(n):
    line = [1]
    for k in range(n):
        line.append(int(line[k] * (n-k) / (k+1)))
    return line

# Расчет n строк треугольника Паскаля
def pascal_n(n):
    triangle = []
    for i in range(n):
        triangle.append(pascal(i))
    return triangle    
   

# преобразование числа к виду: 1000000 -> 1,000,000
def convert_decimal(n):
    n = n[::-1]
    n_txt = ''
    for i, c in enumerate(n):
        if (i + 1) % 3 == 0:
            n_txt += c + ','
        else:
            n_txt += c 
    n_txt = n_txt[::-1].lstrip(',')  
    return n_txt


# упаковка рядом стоящих символов  
# s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'
def zip_symbol(string):
    lst = [[i] for i in string.split()]
    lst_new = [lst[0].copy()]
    
    index_new = 0
    for i in range(1, len(lst)):
        
        if lst[i][0] == lst_new[index_new][0]:
            lst_new[index_new].append(lst[i][0])
        else:
            lst_new.append(lst[i].copy())    
            index_new +=1
    
    return lst_new  
# print(zip_symbol(s) )  


# создание всех возможных подсписков из элементов
# вход 1 2 3 0 
# выход [[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']]
def get_sublists(lst):
    sublists = [[]]  # Пустой список всегда является подсписком
    
    # Проходим по всем возможным длинам подсписков
    for length in range(1, len(lst) + 1):
        # Проходим по всем возможным началам подсписков
        for start in range(len(lst) - length + 1):
            sublist = lst[start:start + length]
            sublists.append(sublist)
    
    return sublists

# Чтение входной строки и формирование списка
input_string = input()
lst = input_string.split()

# Получение всех подсписков
sublists = get_sublists(lst)

# Вывод результата
print(sublists)


#матрица
n = 8
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
for i in range(n):                    # заполняем главную диагональ единицами, а побочную двойками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2

for r in range(n):                    # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()


# выравнивание столбцов    
rows, cols = 3, 4  # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()


# суммы четвертей матрицы(диагональ не учитывается)
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

ch_up = 0
ch_dw = 0
ch_lf = 0
ch_rg = 0

for i in range(n):
    for j in range(n):
        if i < j and i < (n -1 - j):
            ch_up += matrix[i][j]
        elif i > j and i > (n -1 - j):
            ch_dw += matrix[i][j]
        elif i > j and i < (n -1 - j):
            ch_lf += matrix[i][j]
        elif i < j and i > (n -1 - j):
            ch_rg += matrix[i][j]

print(f'Верхняя четверть: {ch_up}')
print(f'Правая четверть: {ch_rg}')
print(f'Нижняя четверть: {ch_dw}')
print(f'Левая четверть: {ch_lf}')    


# Проверка симетричности матрицы
def is_symmetric(matrix):
    # Проверяем, что матрица квадратная
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    
    # Проверяем симметричность относительно главной диагонали
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Пример использования
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
print(is_symmetric(matrix))  # Вывод: True



#отражение элементов(меняем эллементы диагоналей)
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i -1][i] = matrix[n - i -1][i], matrix[i][i]

for m in matrix:
    print(*m)
    

# Поворот матрицы на 90 градусов по часовой стрелке    
def rotate_matrix(matrix):
    n = len(matrix)
    
    # Транспонирование матрицы
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Реверсирование строк
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    
    return matrix    

# ход коня
# на вход позиция, вывести поле с о всеми возможными ходами
def step_horse(pos):
    field = 8
    matrix = [ ['.' for _ in range(field)] for _ in range(field)]
    xpos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    Nx = xpos.index(pos[0])  
    Ny = field - int(pos[1])
    
    matrix[Ny][Nx] = 'N' 
    
    for y in range(field):
        for x in range(field):
            # if (abs(x - Nx) == 1 and abs(y - Ny) == 2) or \
            #     (abs(x - Nx) == 2 and abs(y - Ny) == 1):
            if abs(x - Nx) * abs(y - Ny) == 2:
                    matrix[y][x] = '*' 
    
    for m in matrix:
        print(*m)

step_horse('b6')        

abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2
# Для проверки, является ли заданная квадратная матрица магическим квадратом, нужно выполнить несколько шагов:

# Проверка суммы строк и столбцов: Все строки и столбцы должны иметь одинаковую сумму.
# Проверка диагоналей: Суммы элементов главной и побочной диагоналей должны быть равны сумме строк и столбцов.
# Проверка уникальности чисел: Все числа от 1 до n^2 должны присутствовать в матрице ровно один раз.
def is_magic_square(matrix, n):
    # Вычисляем сумму первой строки (эталонная сумма)
    target_sum = sum(matrix[0])
    
    # Проверка строк
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Проверка столбцов
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target_sum:
            return False
    
    # Проверка главной диагонали
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False
    
    # Проверка побочной диагонали
    if sum(matrix[i][n - 1 - i] for i in range(n)) != target_sum:
        return False
    
    # Проверка уникальности чисел
    numbers = set()
    for row in matrix:
        for num in row:
            if num in numbers or num < 1 or num > n * n:
                return False
            numbers.add(num)
    
    return True



# Заполнение матрицы "змейкой"
# Чтение входных данных
n, m = map(int, input().split())
# Создание матрицы
matrix = [[0] * m for _ in range(n)]
# Заполнение матрицы "змейкой"
num = 1
for i in range(n):
    if i % 2 == 0:
        # Заполнение слева направо
        for j in range(m):
            matrix[i][j] = num
            num += 1
    else:
        # Заполнение справа налево
        for j in range(m - 1, -1, -1):
            matrix[i][j] = num
            num += 1

# Вывод матрицы
for row in matrix:
    print(' '.join(map(str, row)))
    
    
# Заполнение матрицы по диагонали
num = 1
for k in range(n + m - 1):
    # Проход по диагонали
    for i in range(max(0, k - m + 1), min(k + 1, n)):
        j = k - i
        matrix[i][j] = num
        num += 1    
# Если приглядеться, то можно заметить, что в пределах каждой диагонали совпадает сумма индексов i и j
# проходим по всем диагоналям
for d in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == d:
                matrix[i][j] = cnt
                cnt += 1        
                
# Заполнение матрицы по спирали
# Чтение входных данных
n, m = map(int, input().split())

# Создание матрицы
matrix = [[0] * m for _ in range(n)]

# Направления движения: вправо, вниз, влево, вверх
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Начальные координаты и направление
x, y = 0, 0
direction = 0
num = 1

# Границы матрицы
top, bottom, left, right = 0, n - 1, 0, m - 1

while top <= bottom and left <= right:
    # Движение вправо
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    
    # Движение вниз
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    
    if top <= bottom:
        # Движение влево
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
    
    if left <= right:
        # Движение вверх
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

# Вывод матрицы
for row in matrix:
    print(' '.join(map(str, row)))

# Вывод матрицы
for row in matrix:
    print(' '.join(map(str, row)))                
    

# Создание словаря tuple + list    
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for pet in pets:
    result.setdefault(pet[1:], []).append(pet[0])     
    
# создание словаря с подсчетом символов и     
lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{c}_{res[c]}', end=' ')
    else:
        print(c, end=' ')
    res[c] = res.get(c, 0) + 1    

# построение запроса
def build_query_string(params):
    query_str = ''
    params = sorted(params.items())
    for key, value in params:
        query_str += key + '=' + str(value) + '&'
    return query_str.rstrip('&')


    