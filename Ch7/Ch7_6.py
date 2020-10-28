from collections import defaultdict
from collections import OrderedDict

f=open("대한민국헌법_1장.txt",'r')
law=f.readlines()
f.close()
text=""

for line in law:
    text=text+line.strip()+'\n'
text=text.split()

word_count =defaultdict(lambda:0)

for word in text:
    word_count[word]+=1
count =0
for i,v in OrderedDict(sorted(word_count.items(),key=lambda t:t[1], reverse=True)).items():
    print(i,v)
    count+=1
    if count == 5:
        break
