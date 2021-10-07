def factorial(num):
    return 1 if num==0 else num*factorial(num-1)
   # if num==0:
   #     return 1
   # else:
   #     return num*factorial(num-1)


print("factorial: ",factorial(7))
