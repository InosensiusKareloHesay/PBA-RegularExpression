import re

def tokenisasi(data,stopwords):
    for i in range(len(data)):
        for word in stopwords:
            for text in data:
                if text == word:
                    data.remove(text)
    return data

def kataUnik(token):
    dataUnik = []
    #cari data unik
    for word in token:
        if word not in dataUnik:
            dataUnik.append(word)
    #hitung frekuensi data unik
    frekuensiDataUnik = []
    for word in dataUnik:
        counter = 0
        for kata in token:
            if word == kata:
                counter += 1
        frekuensiDataUnik.append(counter)
    #sorting dari besar -> kecil
    for i in range(len(frekuensiDataUnik)):
        for j in range(len(frekuensiDataUnik) - 1):
            if (frekuensiDataUnik[j] < frekuensiDataUnik[j + 1]):
                temp = frekuensiDataUnik[j]
                tempData = dataUnik[j]
                frekuensiDataUnik[j] = frekuensiDataUnik[j + 1]
                dataUnik[j] = dataUnik[j + 1]
                frekuensiDataUnik[j + 1] = temp
                dataUnik[j + 1] = tempData
    return (dataUnik, frekuensiDataUnik)

if __name__ == '__main__':
    # #tugas 4B

    #baca file data
    docB = open("doc_2.txt", "r")
    dataBaca = docB.read()
    docB.close()
    lowerData = dataBaca.lower()
    data = re.findall(r'[a-zA-Z]{2,}',lowerData)
    #baca stopword
    stopword = open("id.stopwords.02.01.2016.txt", "r")
    stopwords = stopword.read()
    stopword.close()
    stopwords = stopwords.split("\n")
    #tokenisasi
    token = tokenisasi(data,stopwords)
    #ambil kata unik dan freq nya
    dataUnik, freqUnik = kataUnik(token)
    #ambil 30 data unik
    for i in range(30):
        StrData = str(dataUnik[i])
        StrFreq = str(freqUnik[i])
        text = StrData + '\t' + StrFreq + '\n'
        output = open('b_kataunik.txt', 'a')
        output.write(text)
        output.close


