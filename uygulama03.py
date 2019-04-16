__author__ = "Sevde Kılıçer"

#Adam Asmaca Oyunu
print("Adam Asmaca Oyununa Hoş Geldiniz. Şimdiden iyi eğlenceler")
print("Doğru tahminler yaparak kelimeyi bulmaya çalışınız.")

from random import choice
while True:
    kelimeler = choice (["ankara", "paris", "londra", "oslo", "madrid", "helsinki", "doha", "tokyo", "sofya", "moskova", "bağdat", "prag", "atina", "berlin", "washington", "edinburgh", "kudüs", "dublin", "stockholm", "brüksel"])
    kelimeler = kelimeler.upper()
    harfsayisi = len(kelimeler)
    print("Hadi başlayalım. Kelime {} harflidir.\n".format(harfsayisi))
    tahminler = []
    hata = []
    cansayısı = 5
    while cansayısı > 0:
        bos = ""
        for girilenharf in kelimeler:
            if girilenharf in tahminler:
                bos = bos + girilenharf
            else:
                bos = bos + " _ "
        if bos == kelimeler:
            print("Tebrikler, Kelimeyi Doğru Buldunuz!")
            break
        print(" Lütfen Kelimeyi Tahmin Ediniz", bos)
        print("Kalan can sayınız", cansayısı)
        Tahmin = input("Lütfen Bir Harf Giriniz :")
        Tahmin = Tahmin.upper()
        if Tahmin == kelimeler:
            print("\n\n Kazandınız Tebrikler! \n\n")
            break
        elif Tahmin in kelimeler:
            rpt = kelimeler.count(Tahmin)
            tahminler.append(Tahmin)
        else:
            print("Üzgünüm Yanlış Tahmin.")
            hata.append(Tahmin)
            cansayısı = cansayısı - 1
    if cansayısı == 0:
        print("\n\n Malesef Hiç Canınız Kalmadı.")
        print("Kelime {}\n\n".format(kelimeler))

    else:
        continue
