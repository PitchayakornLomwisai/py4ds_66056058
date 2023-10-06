#%%
def calculateSum (list_data):
    sum = 0
    if len(list_data) == 0:
        return sum
    else:
        for i in list_data:
            sum = sum + i
        return sum


def calculateProduct(list_data):
    result = 1
    if len(list_data) == 0:
        result = result*0
        return result
    else:
        for i in list_data:
            result = result * i
        print(result)
        return result


def average(list_data):
    sum = 0
    if len(list_data) == 0:
        return sum
    else:
        for i in list_data:
            sum = sum + i
        return sum/len(list_data)


def median(list_data):
    sortedLst = sorted(list_data)
    lstLen = len(list_data)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
def mode(list_data):
    frequency={}
    for number in list_data:
        frequency.setdefault(number,0)
        frequency[number]+=1
    highestFrequencyInLst = max(frequency.values())
    highestFrequencyLst = []
    for number,freq in frequency.items():
        if freq == highestFrequencyInLst:
            highestFrequencyLst.append(number)
    return highestFrequencyLst

if __name__ == '__main__':
    print(calculateSum([]) == 0)
    print(calculateSum([2,4,6,8,10]) == 30)
    print(calculateProduct([]) == 0)
    print(calculateProduct([2,4,6,8,10]) == 3840)
    print(average([1,2,3])==2)
    print(average([1,2,3,1,2,3,1,2,3])==2)
    print(average([12,20,37])==23)
    print(average([0,0,0,0,0])==0)
    print(median([1,2,4,3,5,6,7,9]))
    print(mode([1,2,4,3,5,6,7,9,4,7,7]))


