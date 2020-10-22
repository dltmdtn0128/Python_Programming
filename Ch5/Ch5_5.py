def flatten(data):
    l=[]
    for i in data:
        if type(i) == type(list()):
            l+=(flatten(i))
        else:
            l.append(i)
    return l
example=[[1,2],3,[4,[5,6]],7,[8,9]]
print(flatten(example))
