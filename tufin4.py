

def addAllRecursive(list):
    sum = 0
    for item in list:
        if isinstance(item,int):
            sum+=item
        elif isinstance(item,type(list)):
            sum+=addAllRecursive(item)

    return sum


list = [1, 2, [3, 4], [5, 6]]
print(addAllRecursive(list))