def Fibb(n):
    a=b=counter = 1
    while counter < n:
        print (a,end=' ')
        a,b = b,a+b
        counter += 1
        
Fibb(int(input("Enter a number: ")))
