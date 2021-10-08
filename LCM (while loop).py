a=int(input("Enter The 1st No. = "))
b=int(input("Enter The 2nd No. = "))
c=1
while c<a+b:
    c+=1
    if c%a==0 and c%b==0:
        LCM=c
        print("LCM is =",LCM)
        break
