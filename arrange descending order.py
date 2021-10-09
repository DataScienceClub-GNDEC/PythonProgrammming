print("Arrange No.'s In Descending Order")
a=float(input("Enter the 1st no. = "))
b=float(input("Enter the 2nd no. = "))
c=float(input("Enter the 3rd no. = "))
if a>b:
  if a>c:
      print(a)
      if b>c:
          print(b)
          print(c)
      else:
          print(c)
          print(b)
elif b>c:
    print(b)
    if a>c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    print(b)
    print(a)
      
