n=int(input("Please enter a elements: "))
a=np.array([None]*n)
for i in range(n):
    a[i]=int(input())
key=int(input("Enter the element: "))
val=binary_search(a,start,end,key)
