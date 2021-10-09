# Write a Python program to find whether a queue is empty or not.

# queueList=list(map(int,input("Enter the numbers in the queue: ").split(' ')))
queueList=[]
while(True):
    inputelement=input("Enter the number to add in the queue and stop to end the list: ")
    if inputelement=='stop':
        break
    else:
        queueList.append(int(inputelement))

if len(queueList)==0:
    print("Priyanka, Your Queue is empty.")
else:
    print("Priyanka, your Queue is not empty. ")
