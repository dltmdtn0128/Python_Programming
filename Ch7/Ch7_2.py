
for s in range(2):
    n,l=input().split()
    n=int(n)
    l=int(l)
    list=[]
    for i in range(n,l+1):
        result=2**i
        list.append(result)
    del list[1]
    del list[-2]
    print(list)
