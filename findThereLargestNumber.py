def findThreeLargestNumbers(array):
    largest = [None, None, None]
    for number in array:
        updateLargest(largest, number)
    return largest


def updateLargest(largest, num):
    if largest[2] is None or num > largest[2]:
        shiftAndUpdate(largest,num,2)
    elif largest[1] is None or num > largest[1]:
        shiftAndUpdate(largest,num,1)
    elif largest[0] is None or num > largest[0]:
        shiftAndUpdate(largest,num,0)
def shiftAndUpdate(array,number,index):
    for i in range(index+1):
        if i==index:
            array[i]=number
        else:
            array[i]=array[i+1]

print(findThreeLargestNumbers([11,22,323,42,12,1223]))