print("e ➜ Exit\n")
a=str(input("Enter the 1st no. or (option ➜ e) = "))
import os
if(a=="c"):
        os.system('clear')
        a=str(input("Enter the 1st no. again or (option ➜ c or e) = "))
if(a=="e"):
            exit()
while(True):

    if(a=="e"):
            break
    if(a=="c"):
        os.system('clear')
        a=str(input("Enter the 1st no. again or (option ➜ c or e) = "))
    if(a!="c"):
        print("\t\t  CHOOSE ANY OPERAND TO PERFORM ACTION\n\t\t  ************************************\n\n+      ➜ Addition Of Two Number's \n-      ➜ subtraction Of Two Number's \n*      ➜ Multiplication Of Two Number's \n\      ➜ Dividation Of Two Number's\np(**)  ➜ Power of Number \ns(**)  ➜ Square Root Of Number\n\ne      ➜ Exit\nc      ➜ Clear\n")
        b=str(input("Enter any operand or (option ➜ c or e) = "))
        b = b.lower()
        if(b=="+"):
            c=float(input("Enter the 2nd no. = "))
            d=float(a)+c
            print("The Result of ",a,"+",c," = ",d)
            a=d
            print("\n\n")
        if(b=="-"):
            c=float(input("Enter the 2nd no. = "))
            d=float(a)-c
            print("The Result of ",a,"-",c," = ",d)
            a=d
            print("\n\n")
        if(b=="*"):
            c=float(input("Enter the 2nd no. = "))
            d=float(a)*c
            print("The Result of ",a,"*",c," = ",d)
            a=d
            print("\n\n")
        if(b=="/"):
            c=float(input("Enter the 2nd no. = "))
            if(c==0):
                    print("No. cannot be divided by zero")
            else:
                    d=float(a)/c
                    print("The Result of ",a,"/",c," = ",d)
                    a=d
                    print("\n\n")
        if(b=="p"):
            c=float(input("Enter The Power Of Number = "))
            d=float(a)**c
            print("The Result of ",a,"**",c," = ",d)
            a=d
            print("\n\n")
        if(b=="s"):
            d=float(a)**0.5
            print("The Result of ",a,"** 0.5"" = ",d)
            a=d
            print("\n\n")
        if(b=="e" or a=="e"):
            exit()
        if(b=="c" or a == 'c'):
            os.system('cls')
            a=str(input("Enter the 1st no. again or (option ➜ c or e) = "))


