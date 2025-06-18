
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
            if (abs(x - Nx) == 1 and abs(y - Ny) == 2) or \
                (abs(x - Nx) == 2 and abs(y - Ny) == 1):
                    matrix[y][x] = '*' 
    
    for m in matrix:
        print(*m)

step_horse('b6') 




# lst = input().split() 
lst = '1 2 3 0'.split() 
lst_new = [[]] + lst
n = 0
while n <= len(lst):
    for i, c in enumerate(lst):
        sub = list(c)
        for j in range(i, len(lst) + 1):
            sub += lst[i:j]
            
        lst_new.append([sub])
    n = n + 1    
print(lst_new)    

s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split()
n = 3

def chunked(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


# Формирование списка из символов
lst = s

# Вызов функции chunked
result = chunked(lst, n)

# Вывод результата
print(result)
            
                


s = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'

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

print(zip_symbol(s) )       

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

import numpy as np
np.mean()



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
            ch_dw += matrix[i][j]

print(f'Верхняя четверть: {ch_up}')
print(f'Правая четверть: {ch_rg}')
print(f'Нижняя четверть: {ch_dw}')
print(f'Левая четверть: {ch_lf}')



n, m = int(input()), int(input()) 

matrix = [list(map(int,input().split())) for _ in range(n)]

max_el = matrix[0][0]
max_i = 0
max_j = 0
for i in range(n):
    for j in range(m):
        if max_el < matrix[i][j]:
            max_el = matrix[i][j]
            max_i = i
            max_j = j
            
print(max_i, max_j)  


n, m = int(input()), int(input()) 
matrix = [list(map(int,input().split())) for _ in range(n)]
j1, j2 = list(map(int,input().split()))

for i in range(n):
    matrix[i][j1],  matrix[i][j2] = matrix[i][j2],  matrix[i][j1]

            
for m in matrix:
    print(*matrix)  
    
    

n, m = list(map(int,input().split()))

import numpy as np
matrix = np.zeros((n,m), dtype=int)
count = 0
for i in range(n):
    for j in range(m):
        if i == j or i + j == n-1:
            matrix[i][j] = count
    
for m in matrix:
    print(*m)

n = int(input())

import numpy as np
matrix = np.zeros((n,n), dtype=int)

for i in range(n):
    for j in range(n):
        if ( i <= j and i + j <= n - 1 ) or \
        ( i >= j and i + j >= n - 1 ):
            matrix[i][j] = 1
    
for m in matrix:
    print(*m)
