n=int(input("enter the no. = "))
fact=1
for i in range(1,n):
    fact=fact*n
    n=n-1
print("factorial of the no. is = ",fact)
