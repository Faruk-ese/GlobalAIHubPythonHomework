#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def not_gir():
    name = input("İsmi:")
    surname = input("Soyadı:")
    not1 = input("Not1:")
    not2 = input("Not2:")
    not3 = input("Not3:")

    with open("notes.txt","a",encoding="utf-8") as file:
        file.write(name+" "+surname+":"+not1+","+not2+","+not3+"\n")
def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(":")
    ögrenciAdı = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if (ortalama<=100 and ortalama>=90):
        Harf = "AA"
    elif (ortalama<=89 and ortalama>=80):
        Harf = "BA"
    elif (ortalama<=79 and ortalama>=70):
        Harf = "BB"
    elif (ortalama<=69 and ortalama>=60):
        Harf = "CB"
    elif (ortalama<=59 and ortalama>=50):
        Harf = "CC"
    elif (ortalama<=49 and ortalama>=40):
        Harf = "DC"
    elif (ortalama<=39 and ortalama>=30):
        Harf = "DD"
    elif (ortalama<=29 and ortalama>=20):
        Harf = "FD"
    else:
        Harf = "FF"

    return ögrenciAdı + ":" + Harf + "\n"

def not_oku():

    with open("notes.txt","r",encoding="utf-8") as file:
        for satır in file:
            print(not_hesapla(satır))


def not_kaydet():
    with open("notes.txt","r",encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuçlar.txt","w",encoding="utf-8") as file2:
            for x in liste:
                file2.write(x)

print("""

1-Not girin
2-Not okuma
3-Not kaydetme
4-Çıkış

""")

while True:
    işlem = input("Yapılacak işlemi seçin:")
    if (işlem == "1"):
        print(not_gir())
    elif (işlem == "2"):
        print(not_oku())
    elif (işlem == "3"):
        print(not_kaydet())
    else:
        print("Program sonlanıyorrr")
        break

