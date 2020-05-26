def quickSort(array):
    length=len(array)
    if length<=1:
        return array
    else:
        pivot=array.pop()

    itemsGreater=[]
    itemsLower=[]
    for item in array:
        if(item>pivot):
            itemsGreater.append(item)
        else:
            itemsLower.append(item)

    return quickSort(itemsLower)+[pivot]+quickSort(itemsGreater)
print(quickSort([1,5,2,3,4,12,32,11,2122,1,23,23]))
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(0,len(array)-1-i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
print(bubbleSort([1,5,2,3,4,12,32,11,2122,1,23,23]))
