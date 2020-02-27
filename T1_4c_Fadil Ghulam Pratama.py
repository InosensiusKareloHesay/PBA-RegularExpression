import re

docC = open("doc_3.srt","r")
text = docC.read()
docC.close()
regex = r"(\d{1,4}\s.*|<i>|</i>|<font.*)"
hasil = re.sub(regex,"",text)
hasil2 = hasil.split("\n")
for i in range(len(hasil2)):
    if(len(hasil2[i])!=0):
        StringSub = hasil2[i]+'\n'
        output = open("c_subtitle.txt","a")
        output.write(StringSub)
        output.close()