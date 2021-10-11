# Write a Python program to create a FIFO queue

queueList=[]
while(True):
    choose=input("Enter 'insert' to enter element in queue and 'remove' to discard the element and 'stop' to stop inserting and removing : ")
    if choose=='remove':
        if(len(queueList)>=1):
            queueList.remove(queueList[0])
    elif choose=='insert':
        element=int(input("Enter the element to insert in the queue: "))
        queueList.append(element)
    elif choose == 'stop':
        break
    else:
        print("Kindly always enter choice carefully.")

print("Priyanka, At Last the QueueList is: ",queueList)