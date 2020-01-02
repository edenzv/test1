
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def give3rdItemBest(list):
    return list[2::3]

def give3rdItem(list):
    newList = []
    num = 1
    for item in list:
        if num == 3:
            newList.append(item);
            num = 1
        else:
            num += 1
    return newList

def give3rdItemNew(list):
    newList = []
    for num in range(len(list)):
        if ((num+1)%3==0):
            newList.append(list[num])
    return newList


print("list best:")
print(give3rdItemBest(list))

print("list regular:")
print(give3rdItem(list))

print("list regular new:")
print(give3rdItemNew(list))
# x = int(input("Please enter integer:"))
#
# print("The x is :"+str(x))