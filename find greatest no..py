print("*****To Find The Greatest No.*****") 
a=float(input("enter the 1st no."))
b=float(input("enter the 2nd no."))
c=float(input("enter the 3rd no."))
d=float(input("enter the 4th no."))
if a>b:
    if a>c:
        if a>d:
            print(a,"is Greatest no.")
        else:
            print(d,"is Greatest no.")
    elif c>d:
        print(c,"is Greatest no.")
    else:
        print(d,"is Greatest no.")
elif b>c:
    if b>d:
        print(b,"is Greatest no.")
    else:
        print(d,"is Greatest no.")
elif c>d:
    print(c,"is Greatest no.")
else:
    print(d,"is Greatest no.")
            

