a=int(input("Enter the no. = "))
d=""
b=a
while(a):
    r=a%10
    d=d+str(r)
    a=a//10
    if a==0:
        break
if b==int(d):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
