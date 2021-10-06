list=[]
print("Enter length of the list")
lenOfTheList=int(input());
print("Enter the list of numbers")
for i in range(0,lenOfTheList):
    num=input()
    list.append(int(num))

print(list)
index=len(list)+2
print("Enter Search element")
search_element=int(input())
for i in range(0, len(list)):
    if list[i]==search_element:
        index=i;
        break

if(index==len(list)+2):
    print("Element",search_element," is not in the list")
else:
    print("Element ",search_element,"is at the index",index, " of the list.")
