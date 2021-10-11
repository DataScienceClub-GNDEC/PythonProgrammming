a=int(input("Enter the no. = "))
c=0
for i in range(a):
    r=a%10
    print(r,end="")
    a=a//10
    if a==0:
        break
