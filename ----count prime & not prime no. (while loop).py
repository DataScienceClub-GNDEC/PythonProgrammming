n=int(input("Enter The Number's = "))
x=0
h=0
j=0
i=2
while j<n:
    j+=1
    b=1
    a=n%10
    if a>1:
        while (i<a):
            i+=1
            if a%i==0:
                b=0
                break
            i+=1
        if b==0:
            h=h+1
        else:
            x=x+1
    else:
        h+=1
    n=n//10
    if n==0:
        break
print("Total No. Of Prime Numbers Are = ",x)
print("Total No. Of Not Prime Numbers Are = ",h)
                
