file=input()
file=file.split()

result = list(map(lambda x:'{0:03d}'.format(int(x.split('.')[0]))+'.'+x.split('.')[1],file))
print(result)
