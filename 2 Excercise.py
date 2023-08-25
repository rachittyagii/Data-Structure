import numpy as np
def sort(a,n):
   for i in range(1,n):
    key=a[i]
    j=i-1
    while(a[j]>key and j>=0):
       a[j+1]=a[j]
       j=j-1
       a[j+1]=a[j]
       return a

n=int(input("Enter no of elements"))
np.array([None]*n)
for i in range(n):
   a[i]=int(input())
print(a)
b=sort(a,n)
print(b)