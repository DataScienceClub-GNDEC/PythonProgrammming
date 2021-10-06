list=[]
print("Enter length of the list")
lenOfTheList=int(input());
print("Enter the list of numbers")
for i in range(0,lenOfTheList):
    num=input()
    list.append(int(num))

print(list)
print("Enter Search element")
search_element=int(input())

list.sort()

print(list)
start_index=0
end_index=len(list)-1
index = len(list) + 2
def binary_search(list, start_index, end_index, search_element):
    print("start_index: ", start_index)
    print("end_index: ", end_index)
    mid = int((start_index+end_index)/ 2)
    print("mid : ",mid)
    if (end_index>=start_index):
        if (list[mid]==search_element):
            print("Element ",search_element,"is at the index",mid, " of the list.")
        elif (list[mid]<search_element):
             binary_search(list, mid+1, end_index, search_element)
        elif (list[mid]>search_element):
            binary_search(list, start_index, mid-1, search_element)
    else:
        print("Search Unsuccessful")

binary_search(list, start_index, end_index, search_element)

