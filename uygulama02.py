print("Edebiyat bilginizi ölçmek ve görmek ister misiniz")
print("Aşağıdaki soruları cevaplayınız")
print("*************************************************")

sorular = ['Türk Edebiyatında ilk realist roman kime aittir?',
           'Tanzimat Dönemi Edebiyatının tarihi nedir?',
           'Ülkemize ilk nobel ödülünü kazandıran yazarımız kimdir?',
           'Dünya Edebiyatında ilk modern romanın adı nedir?',
           'Türk Edebiyatında ilk kadın yazarımız kimdir?']
cevaplar = ['A', 'C', 'B', 'D', 'C']
cevapA = ['Recaizade Mahmut Ekrem', '1859-1890','Orhan Kemal', 'Decameron', 'Halide Edip Adıvar']
cevapB = ['Namık Kemal', '1861-1892', 'Orhan Pamuk', 'Madama Bovary', 'Tomris Uyar']
cevapC = ['Muallim Naci', '1860-1895', 'Orhan Asena', 'Diyojen', 'Fatma Aliye']
cevapD = ['Şinasi', '1860-1892', 'Sezai Karakoç', 'Cervantes', 'Tezer Özlü']

puan = 0
for x in range(len(sorular)):
    print("Soru" + str(x + 1) + ":" + sorular[x])
    print("A) " + cevapA[x])
    print("B) " + cevapB[x])
    print("C) " + cevapC[x])
    print("D) " + cevapD[x])
    cevap = input("Lütfen cevabınızı giriniz : ")
    if cevaplar[x] == cevap.upper():
        puan += 1

#Total puan
print("Tebrikler testi bitirdiniz")
print("Aldığınız not:" + str(int((puan / len(sorular)) * 100)))
input()