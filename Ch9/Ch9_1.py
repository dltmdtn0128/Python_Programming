from functools import reduce

i=int(input())
result = reduce(lambda x,y:x*y,range(1,i+1))
print(format(result,","))
