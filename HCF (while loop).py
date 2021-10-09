a=int(input("Enter The 1st No. = "))
b=int(input("Enter The 2nd No. = "))
if a>b:
    x=b
else:
    x=a
i=1
while i<x+1:
    i+=1
    if a%i==0 and b%i==0:
        Hcf=i
print("Hcf is =",Hcf)
