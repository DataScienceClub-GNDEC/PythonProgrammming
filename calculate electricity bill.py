#billing electric system
u=float(input("Enter the total units = "))
a=0
b=0
c=0
d=0
if(u>=401):
    a=u-400
    u=u-a
    a=a*6.50
if(u>=201):
    b=u-200
    u=u-b
    b=b*4.50
if(u>=101):
    c=u-100
    u=u-c
    c=c*2.50
if(u>0):
    d=u-0
    d=d*1.50
print("Total bill = ",a+b+c+d)
