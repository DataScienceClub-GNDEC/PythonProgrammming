print("Arrange No.'s In Ascending Order")
a=float(input("Enter the 1st no. = "))
b=float(input("Enter the 2nd no. = "))
c=float(input("Enter the 3rd no. = "))
if(a>b):
    swap=a
    a=b
    b=swap
if(a>c):
    swap=a
    a=c
    c=swap
if(b>c):
    swap=b
    b=c
    c=swap
print("\n",a)
print("\n",b)
print("\n",c)
