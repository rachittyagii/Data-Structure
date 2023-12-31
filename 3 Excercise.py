import numpy as np
def binary_search(a,start,end,key):
    if end>=start:
        mid=(start+end)//2
    if a[mid]==key:
        return mid
    elif a[mid]>key:
        start=mid+1
        binary_search(a,start,end,key)
    else:
        end=mid-1
        binary_search(a,start,end,key)
    return -1

n=int(input("Please enter a elements: "))
a=np.array([None]*n)
for i in range(n):
    a[i]=int(input())
key=int(input("Enter the element: "))
start=0
end=n-1
val= binary_search(a,start,end,key)
if val==-1:
    print("Search unsuccessful")
else:
    print("Search successful at index",val)
