# Write a Python program to insert items into a list in sorted order.

given_list=[]
while(True):
    inputelement=input("Enter the number to add in the given list and stop to end the list: ")
    if inputelement=='stop':
        break
    else:
        given_list.append(int(inputelement))

print(given_list)
given_list.sort()
print(given_list)
while(True):
    choice=input("Enter the number to insert in the given list and stop to end the list: ")
    if choice=='stop':
        break
    else:
        for j in range(0,len(given_list)):#given_list
            if (len(given_list)==1):
                if int(choice)>given_list[0]:
                    given_list.insert(1, int(choice))
                    break
                else:
                    given_list.insert(0, int(choice))
                    break
                print(given_list)
            elif (j<len(given_list)-1):
                if given_list[j]<=int(choice) and given_list[j+1]>=int(choice):
                    given_list.insert(j+1, int(choice))
                    break
            elif (j==len(given_list)-1):
                if given_list[j]<=int(choice):
                    given_list.insert(j+1, int(choice))
                    break

print("Priyanka, After inserting the elements, List:",given_list)
