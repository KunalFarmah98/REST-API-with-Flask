# *args specifies variable number of arguments, we don't care how many 
# are passed, it will work

def add(*args):
    total = 0
    for arg in args:
        total+=arg
    return total


print(add(1,2,3,4))

# **dictionary collects all the keys and add them to named arguments for the function
# the name of arguments and the keys must be same for it to work

def func(X,Y):
    print("{}, {}".format(X,Y))
dict = {"X":1,"Y":"YES"}

func(**dict)

# mixing args with a compulsory argument
""" It can cause some funny bugs, so be careful"""

def doit(*args, operator):
    if(operator=="+"):
        # NOTE: WE HAVE TO COLLECT EACH ARGUMENT SEPARATELY, ELSE THE ENTIRE TUPPLE
        # WILL BE PASSED
        print (add(*args))
        # this is error
        # print (add(args))
        # sum is a build in function and handles the case
        print (sum(args))

doit(1,2,3,4,operator="+")