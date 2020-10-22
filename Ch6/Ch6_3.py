f= open("Ch6_Hey_Jude.txt",'r')
jude_lyric=f.readlines()
f.close()

contents = ""

for line in jude_lyric:
    contents = contents + line.strip()+" "

contents=contents.replace("-"," ")
contents=contents.replace(",","")
contents=contents.replace("(", "")
contents=contents.replace(")", "")

l_of_jude = contents.count(" ")

print(l_of_jude)
