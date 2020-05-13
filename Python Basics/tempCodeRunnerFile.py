def search(seq, expected,finder):
    for ele in seq:
        if(getName(ele)==expected):
            return True
    raise(RuntimeError("Couldn't find {}".format(expected)))

def getName(vals):
    return vals["name"]


vals = [
        {"name":"Kunal","age":22},
        {"name":"Jhasa","age":21},
        {"name":"Harshit","age":22}
        ]

print(search(vals,"Kunal",getName))
print(search(vals,"SAX",getName))
print(search(vals,"Jhasa",lambda vals: vals["name"]))