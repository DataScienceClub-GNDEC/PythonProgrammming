a=int(input("enter the no. = "))
c=0
while a:
    r=a%10
    c=c+r
    a=a//10
    if a==10:
        break
print(c)
