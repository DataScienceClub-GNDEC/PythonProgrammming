def mergeSort(list):
    print("List: ", list)
    if len(list)>1:
        mid=len(list)//2;
        LeftHalf=list[:mid]
        RightHalf=list[mid:]
        print("Left half list: ",LeftHalf)
        print("Right half list: ", RightHalf)
        print()
        mergeSort(LeftHalf)
        mergeSort(RightHalf)

        i=j=k=0;
        while(i<len(LeftHalf) and j<len(RightHalf)):
            if i<len(LeftHalf) and j<len(RightHalf):
                if LeftHalf[i]<RightHalf[j]:
                    list[k]=LeftHalf[i]
                    i=i+1
                else:
                    list[k]=RightHalf[j]
                    j=j+1
                k=k+1

        while(i<len(LeftHalf)):
            list[k]=LeftHalf[i]
            i=i+1
            k=k+1


        while(j<len(RightHalf)):
            list[k]=RightHalf[j]
            j=j+1
            k=k+1
    print("Sorted List: ", list)
    return list

list=[34,3432,5,3,53,75]
print("Final Sorted List: ",mergeSort(list))

