while(1==1):
    print("1)Find Inclusive GST In Cost Of Service \n2)Find Exclusive GST On Cost Of Service \n3)Find Inclusive GST In Cost Of Product \n4)Find Exclusive GST On Cost Of Product \n5)Exit")
    a=int(input("*****Choose No. From The List To Perform a Task***** = "))
    if(a==1):
        print("********INCLUSIVE GST ON SERVICE********\n")
        amt=int(input("Enter your actual amount without GST = "))
        exclusive=amt*1.18
        print("Amount after adding exclusive GST is = ",exclusive)
        print("\n\n")

    if(a==2):
        print("********EXCLUSIVE GST ON SERVICE********\n")
        fee=int(input("Enter your course fee including GST = "))
        actual=fee/1.18
        print("Your actual course fee is = ",actual)
        inclusive=fee-actual
        print("GST which is added in your fee is = ",inclusive)
        print("\n\n")

    if(a==3):
        print("********INCLUSIVE GST ON PRODUCT********\n")
        amt=int(input("Enter actual cost of product without GST = "))
        exclusive=amt*1.05
        print("Amount after adding exclusive GST is = ",exclusive)
        print("\n\n")

    if(a==4):
        print("********EXCLUSIVE GST ON PRODUCT********\n")
        cost=int(input("Enter cost of product including GST = "))
        actual=cost/1.05
        print("Actual cost of product is = ",actual)
        inclusive=cost-actual
        print("GST which is added in the cost of product is = ",inclusive)
        print("\n\n")

    if(a==5):
        exit(5)

