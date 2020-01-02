# # Build and return a list
# def firstn(n):
#     num, nums = 0, []
#     while num < n:
#         nums.append(num)
#         num += 1
#     print(nums)
#     print(num)
#     return nums
#
# sum_of_first_n = sum(firstn(10))
#
# print(sum_of_first_n)


# Using the generator pattern (an iterable)
class firstn:
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(firstn([1,23]))

print(sum_of_first_n)