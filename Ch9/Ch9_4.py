def vector_sub(*args):
    return[t[0]*2-sum(t) for t in zip(*args)]

print(vector_sub([10,9,8],[1,2,3],[3,4,5],[1,1,1]))
