import numpy as np

def sort(a, n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a

n = int(input("Enter no of elements: "))
a = np.array([None] * n)  # Corrected array initialization

for i in range(n):
    a[i] = int(input())

print(a)
b = sort(a, n)
print(b)
