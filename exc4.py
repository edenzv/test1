# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield "call 1"
    yield "this is call 2"
    yield "this is call 3"


print(simpleGeneratorFun())

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

