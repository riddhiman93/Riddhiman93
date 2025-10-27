fterm,sterm=0,1
n=int(input("Fibonacci Series upto terms:"))
for i in range(1,n+1):
    print(fterm,end=" ")
    nterm=fterm+sterm
    fterm=sterm
    sterm=nterm