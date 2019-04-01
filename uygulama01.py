# Puan Tanımlama
x = 0
puan = x

# Soru 1
print("Atatürk kaç yılında doğmuştur?")
cevap_1 = input(":")
if cevap_1.lower() == "1881":
    print("Cevabınız doğru")
    x = x + 1
else:
    print("Yanlış cevap")
# Soru 2
print("İstanbulu kim fethetmiştir?")
cevap_2 = input(":")
if cevap_2.title() == "Fatih Sultan Mehmet":
    print("Cevabınız doğru")
    x= x+1
else:
    print("Yanlış cevap")
# Soru 3
print("Dünyanın ilk kadın savaş uçağı pilotu kimdir?")
cevap_3 = input(":")
if cevap_3.title() == "Sabiha Gökçen":
    print("Cevabınız doğru")
    x= x+1
else:
    print("Yanlış cevap")
# Soru 4
print("Cumhuriyet ne zaman ilan edilmiştir?")
cevap_4 = input(":")
if cevap_4.title() == "29 Ekim 1923":
    print("Cevabınız doğru")
    x= x+1
else:
    print("Yanlış cevap")
#Soru 5
print("İstiklal marşı yazarı kimdir?")
cevap_5 = input(":")
if cevap_5.title() == "Mehmet Akif Ersoy":
    print("Cevabınız doğru")
    x= x+1
else:
    print("Yanlış cevap")

#Total puan
print("Testi tamamladınız tebrikler")
puan = float(x / 5) * 100
print("Final puanı: " ,"%",puan)