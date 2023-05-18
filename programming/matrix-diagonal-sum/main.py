import time
import random


# arr = [[random.randint(1, 100) for i in range(2000)] for j in range(2000)]
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
n = len(arr)

start_time1 = time.time()
s = 0
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            s += arr[i][j]

print(s)
end_time1 = time.time()
start_time2 = time.time()

s = 0
for i in range(n):
    s += arr[i][i]
    s += arr[i][n - i - 1]

if n % 2 == 1:
    s -= arr[n // 2][n // 2]


print(s)
end_time2 = time.time()

print("Time1: ", end_time1 - start_time1)
print("Time2: ", end_time2 - start_time2)
