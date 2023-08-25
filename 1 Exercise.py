import numpy as np
n=int(input("Enter no of elements"))
a=np.array([None]*n)
for i in range(n):
    a[i]=int(input())
print(a)
key=int(input("Enter element to be searched"))
for i in range(n):
    if(a[i]==key):
        print("Search print succesfully")
        break
else:
    print("Search unsuccesful")
max=a[0]
min=max
for i in range(i,n):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
        print("Max is",max,"and min is",min)

       