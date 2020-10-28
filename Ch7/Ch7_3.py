a=[]
round = int(input())
for i in range(round+1):
    inp=input()
    if inp.split()[0] == 'push':
        a.append(int(inp.split()[1]))

    elif inp =='pop':
        if not a:
            print(-1)
        elif len(a) > 0:
            print(a.pop(0))


    elif inp == 'size':
        print(len(a))
    elif inp == 'empty':
        if len(a) == 0: print(1)
        if len(a) > 0: print(0)
    elif inp == 'front':
        if len(a)==0:
            print(-1)
        elif len(a) > 0:
            print(a[0])
    elif inp == 'back':
        if len(a)==0:
            print(-1)
        elif len(a) > 0:
            print(a[-1])
