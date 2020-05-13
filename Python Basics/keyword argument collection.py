# **kwargs collects all keyword arguments
""" kwargs is a dictionary keyed by name of arg """
def fun(**kwargs):
    print(kwargs)

details = {"name":1, "age":2}

# PARAMETER HAS TO BE A DICTIONARY
fun(name="Kunal", age=2)

# **args same
def fun1(name, age):
    print (name)
    print (age)

fun1(**details)


""" COMBO OF ARGS AND NAMED ARGS IS USED TO ACCEPT UNLIMITED NUMBER OF ARGUMENTS """
def gg(*args, **kwargs):
    print(args)
    print(kwargs)

gg(1,2,3,4,"kunal",name="kunal",age=21)


