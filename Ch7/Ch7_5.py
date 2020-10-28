
word = input()
s_word = word.split()
num = input()
s_num=num.split()
dictionary=dict(zip(s_word,s_num))

dictionary={key:value for key,value in dictionary.items() if value != '30' and key != 'delta'}
print(dictionary)
