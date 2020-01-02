
class give3rdItem:
    def __init__(self, list):
        self.list = list
        self.num, self.newList = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if (self.num+1)%3 == 0:
            # self.newList.append(self.list[self.num])
            self.num+=1
            return self.list[self.num]
        if self.num == len(self.list):
            raise StopIteration()

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
newlist = give3rdItem(list)
print("test")