price = input("가격 입력 : ")
l_price=[]
s_price= price.split(";")
for i in s_price:
    l_price.append(int(i))
l_price.sort(reverse=True)

for i in l_price:
    print("{:10,d}".format(i))
