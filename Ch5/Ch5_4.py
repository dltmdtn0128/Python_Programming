def fact(n):
    fac =1
    if n==1:
        return fac
    else:
        fac =n*fact(n-1)
        return fac
n= int(input())
temp=str(fact(n)).rstrip('0')
for i in range(-5,0):
    print(temp[i],end='')
