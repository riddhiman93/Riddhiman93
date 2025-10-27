a=[1,2,3,4,5,6,7,8,9,10]
print(a)
e=int(input("Element to search for in the array:"))
n=len(a)
s=0
for i in range(n):
    if a[i]==e:
        s=a[i]
if  s==0:
    print("The required element is not found in the array.")
else:
    print("The required element is found in the array:",s)


