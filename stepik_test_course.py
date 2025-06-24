


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
