r,s=input().split()
r=int(r)
p='' #새 문자열

for i in range(len(s)):
    p=s[i]*r
    print(p,end='')
