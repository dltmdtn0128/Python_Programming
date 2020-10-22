f= open("Ch6_Hey_Jude.txt",'r')
jude_lyric=f.readlines()
f.close()

contents = ""

for line in jude_lyric:
    contents = contents + line.strip() + "\n"

c_word = input("단어 입력 : ")

n_of_jude = contents.lower().count(c_word.lower())
print(c_word," word count is ",n_of_jude)

r_word = input("이름 입력 : ")

r_lyric = contents.replace('Jude',r_word)

print(r_lyric)
