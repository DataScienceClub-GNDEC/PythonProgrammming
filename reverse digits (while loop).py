x=int(input("Enter the no. = "))
c=0
while(x):
    y=x%10
    print(y,end="")
    x=x//10
    if x==0:
        break
