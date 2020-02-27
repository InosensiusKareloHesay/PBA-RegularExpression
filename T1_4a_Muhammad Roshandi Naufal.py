import re
import json

dokumen = open("doc_1.txt", encoding="utf-8")
dokumen = dokumen.read()
dictBook = {}

# Mencari Author
regexNama = r"(^\w+, \w+; \w+, \w+; \w+, \w+; \w+, \w+; \w+, \w+|" \
            r"^\w+, \w.; \w+, \w+ \w+.; \w+, \w.; \w+, \w.|^\w+, \w+; \w+, \w+; " \
            r"\w+, \w+|^\w+, \w+; \w+, \w+ \w?\.?|^\w+, \w+ \w+; \w+, \w+.|^\w+, " \
            r"\w+; \w+ \w+.|^\w+, \w+ \w?\.?|^\w+ \w+\.|^\w+)"
nama = re.findall(regexNama,dokumen, re.MULTILINE)

# Mencari Judul
judul = re.findall('("[A-Za-z :-]+"|\. [A-Za-z ]+\. [A-Za-z] [a-z]+.| \([a-z]+\) [a-z]+.|\. [A-Za-z, ]+: [A-Za-z ]+\.|^P[A-Za-z ]+\(|\. [A-Za-z ]+\(\w+\)\.|\. H[A-Za-z ()]+.| Fo[A-Za-z ]+.| D[A-Za-z ]+g\.| Ex[A-Za-z ]+\.)', dokumen, re.MULTILINE)

# Mencari Tahun
tahun = re.findall("( \d{4}\.\s|\(\d{4}\)|\/\d{4}| \d{4} |20\d{2}\.$)", dokumen, re.MULTILINE)

regex = r'\)|\.| |\s|\(|;|,'
tahun1 = re.sub(regex,"", str(tahun))

i = 1
for x,y,z in zip(judul,tahun,nama):
    dictBook['book' + str(i)] = {'author': z, 'year': y, 'title': x}
    i+=1

with open('a_judul.json', 'w') as fp:
    json.dump(dictBook, fp)