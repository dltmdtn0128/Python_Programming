
na = open('파이썬1_수강생_이름.txt','r')
num=open('파이썬1_수강생_학번.txt','r')
major=open('파이썬1_수강생_학과.txt','r')

name = na.readlines()
no = num.readlines()
ma = major.readlines()
na.close()
num.close()
major.close()

n_list= [i.rstrip() for i in name]
no_list=[i.rstrip() for i in no]
ma_list =[i.rstrip() for i in ma]
t_list=[]

for i,j,k in zip(n_list, no_list, ma_list):
    t_list.append((i,j,k))
print(t_list)
t_dict= {t_list[i][0]:[t_list[i][1],t_list[i][2]] for i in range(len(t_list))}
print(t_dict)
s_dict = dict(sorted(t_dict.items(),key=lambda x:x[0]))
print(s_dict)
count=0
print('No.','\t   ','학번     이름\t  학과')
for name,info in s_dict.items():
    count+=1
    print(count,'\t',info[0],name,info[1])
