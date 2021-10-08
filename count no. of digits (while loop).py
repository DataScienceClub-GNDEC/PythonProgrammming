a=int(input("Enter the no. = "))
c=0
while a>0:
        c+=1
        a=a//10
        if a==0:
            break
print("Total no. of digits are =",c)

