itemsList = []

def insert(itemsList, item):
    if(len(itemsList) == 0):
        itemsList.append(item)
    else:
        for i in range(len(itemsList)):
            if(item > itemsList[i]):
                index = i
            elif(item < itemsList[i]):
                index = i-1
                break
                
        itemsList = itemsList[:index+1] + [item] + itemsList[index+1:]    
    return itemsList

ch = 1
while ch!='exit':
    ch =input("Enter element to insert\nEnter 'exit' to exit\n")
    if ch=="exit":
        break
    else:
        item = int(ch)
        itemsList = insert(itemsList, item)
        print(itemsList)