VeriTabani = {}
okulNoListesi = list()

def ogrenciNotlariniEkle():
    global sozluk, Odev_1, Odev_2, Kisa_Sinav_1, Kisa_Sinav_2, Proje_1, Vize_1, Final_1, answer, ad, soyad, okulNo
    sozluk = {}
    print(20 * "-")

    answer = False
    okulNo = int(input("Ogrenci numarası: "))
    while answer!=True:
        ad = str(input("Ogrenci adi: "))
        while not answer:
            if len(ad)<3:
                print("Tekrar giriniz")
                ad = str(input("Ogrenci adi: "))
            break
        soyad = str(input("Ogrenci soyadi: "))
        while not answer:
            if len(soyad)<3:
                print("Tekrar giriniz")
                soyad = str(input("Ogrenci soyadi: "))
            answer=True
    print(20 * "-")

    answer=False
    while answer!=True:
        Odev_1 = int(input("Birinci Ödev Not Aralığı 0-200 \n" "Birinci Ödevi Giriniz :" ))
        print(20 * "-")
        while not answer:
            if (Odev_1 < 0 or Odev_1 > 200):
                Odev_1 = int(input("Yanlış not girdiniz tekrar giriniz (0-200): "))
            else:
               break

        Odev_2 = int(input("İkinci Ödevi Giriniz 0-200 \n" "İkinci Ödevi Giriniz :"))
        print(20 * "-")
        while not answer:
            if (Odev_2 < 0 or Odev_2 > 200):
                Odev_2 = int(input("Yanlış not girdiniz tekrar giriniz (0-200): "))
            else:
                break

        Kisa_Sinav_1 = int(input("Kısa Sınavı Not Aralığı 0-100 \n" "Birinci Kısa Sınavı Giriniz :"))
        print(20 * "-")
        while not answer:
            if (Kisa_Sinav_1 < 0 or Kisa_Sinav_1 > 100):
                Kisa_Sinav_1 = int(input("Yanlış not girdiniz tekrar giriniz (0-100): "))
            else:
                break

        Kisa_Sinav_2 = int(input("Kısa Sınavı Not Aralığı 0-100 \n" "İkinci Kısa Sınavı Giriniz :"))
        print(20 * "-")
        while not answer:
            if (Kisa_Sinav_2 < 0 or Kisa_Sinav_2 > 100):
                Kisa_Sinav_2 = int(input("Yanlış not girdiniz tekrar giriniz (0-100): "))
            else:
                break

        Proje_1 = int(input("Proje Not Aralığı 0-400 \n" "Proje Notunu Giriniz :"))
        print(20 * "-")
        while not answer:
            if (Proje_1 < 0 or Proje_1 > 400):
                Proje_1 = int(input("Yanlış not girdiniz tekrar giriniz (0-400): "))
            else:
                break

        Vize_1 = int(input("Vize Not Aralığı 0-400 \n" "Vize Notunu Giriniz :"))
        print(20 * "-")
        while not answer:
            if (Vize_1< 0 or Vize_1 > 400):
                Vize_1 = int(input("Yanlış not girdiniz tekrar giriniz (0-400): "))
            else:
                break

        Final_1 = int(input("Final Not Aralığı 0-600 \n" "Final Notunu Giriniz :"))
        print(20 * "-")
        while not answer:
            if (Final_1 < 0 or Final_1 > 600):
                Final_1 = int(input("Yanlış not girdiniz tekrar giriniz (0-600): "))
            else:
                answer=True

    not_toplam = Odev_1 + Odev_2 + Kisa_Sinav_1 + Kisa_Sinav_2 + Proje_1 + Vize_1 + Final_1
    not_ortalamasi = not_toplam * 0.05
    okulNoListesi.append(okulNo)

    sozluk = {"okulNo": okulNo, "ad": ad, "soyad": soyad, "Ödev 1": Odev_1, "Ödev 2": Odev_2,"Kısa Sınav 1": Kisa_Sinav_1, "Kısa Sınav 2": Kisa_Sinav_2, "Proje 1": Proje_1, "Vize": Vize_1,"Final": Final_1, "Not Ortalaması": not_ortalamasi}
    VeriTabani[okulNo] = sozluk

    if (not_ortalamasi >= 90 and not_ortalamasi <= 100):
        sozluk["Notu"]="AA"
    if (not_ortalamasi >= 80 and not_ortalamasi <= 89):
        sozluk["Notu"] = "BA"
    if (not_ortalamasi >= 70 and not_ortalamasi <= 79):
        sozluk["Notu"] = "BB"
    if (not_ortalamasi >= 60 and not_ortalamasi <= 69):
        sozluk["Notu"] = "CB"
    if (not_ortalamasi >= 50 and not_ortalamasi <= 59):
        sozluk["Notu"] = "CC"
    if (not_ortalamasi >= 40 and not_ortalamasi <= 49):
        sozluk["Notu"] = "DC"
    if (not_ortalamasi >= 20 and not_ortalamasi <= 39):
        sozluk["Notu"] = "DD"
    if (not_ortalamasi >= 00 and not_ortalamasi <= 19):
        sozluk["Notu"] = "FF"


def ogrencileriListele():
    for i in okulNoListesi:
        print("Ogrenci Numarasi: {0} \t Adı: {1} \t Soyadı: {2} \t Ödev_1: {3} \t Ödev_2: {4} \t Kısa_Sınav_1: {5} \t Kısa_Sınav_2: {6} \t Proje_1: {7} \t Vize_1: {8} \t Final_1: {9} \t Not_Ortalaması: {10} \t Notu: {11}"
              .format(VeriTabani[i].get("okulNo"), VeriTabani[i].get("ad"), VeriTabani[i].get("soyad"),VeriTabani[i].get("Ödev 1"), VeriTabani[i].get("Ödev 2"),
                      VeriTabani[i].get("Kısa Sınav 1"),VeriTabani[i].get("Kısa Sınav 2"), VeriTabani[i].get("Proje 1"), VeriTabani[i].get("Vize"),
                      VeriTabani[i].get("Final"), VeriTabani[i].get("Not Ortalaması"), VeriTabani[i].get("Notu")))
        print(20 * "-")


def OgrenciNotlariniSil():
    silinecek = int(input("Silmek istediginiz Ogrencinin okul numarasini giriniz: "))
    if silinecek in VeriTabani:
        del VeriTabani[silinecek]
        okulNoListesi.remove(silinecek)
        print("Öğrencinin kaydı silinmiştir.")
    else:
        print("Böyle bir öğrenci yoktur")


def notGuncelleme():
    global Odev_1, Odev_2, Kisa_Sinav_1, Kisa_Sinav_2, Proje_1, Vize_1, Final_1, not_ortalamasi, ad, soyad
    while 1:
        print("Guncelleme yapmak istediginizi seciniz.. \n[1] Adı \n[2] Soyadı \n[3] Ödev_1 \n[4] Ödev_2 \n[5] Kısa_Sınav_1 \n[6] Kısa_Sınav_2 \n[7] Proje_1  \n[8] Vize_1 \n[9] Final_1 \n[Q veya q] Cikis")
        gSecim = input("Seçiminiz: ")
        if gSecim == "q" or gSecim == "Q":
            break
        ogrenciNo = int(input("Guncelleme yapmak istediginiz ogrenci numarasini giriniz: "))
        if ogrenciNo in VeriTabani :
            if gSecim == "1":
                ad = input("Ogrenci adi giriniz: ")
                VeriTabani[ogrenciNo]["ad"] = ad
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "2":
                soyad = input("Ogrenci soyadi giriniz: ")
                VeriTabani[ogrenciNo]["soyad"] = soyad
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "3":
                Odev_1 = int(input("Ogrenci Ödev 1 Giriniz: "))
                VeriTabani[ogrenciNo]["Ödev 1"] = Odev_1
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "4":
                Odev_2 = int(input("Ogrenci Ödev 2 Giriniz: "))
                VeriTabani[ogrenciNo]["Ödev 2"] = Odev_2
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "5":
                Kisa_Sinav_1 = int(input("Ogrenci Kısa Sınav 1 Giriniz: "))
                VeriTabani[ogrenciNo]["Kısa Sınav 1"] = Kisa_Sinav_1
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "6":
                Kisa_Sinav_2 = int(input("Ogrenci Kısa Sınav 2 Giriniz: "))
                VeriTabani[ogrenciNo]["Kısa Sınav 2"] = Kisa_Sinav_2
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "7":
                Proje_1 = int(input("Ogrenci Proje 1 Giriniz: "))
                VeriTabani[ogrenciNo]["Proje 1"] = Proje_1
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "8":
                Vize_1 = int(input("Ogrenci Vize 1 Giriniz: "))
                VeriTabani[ogrenciNo]["Vize 1"] = Vize_1
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            elif gSecim == "9":
                Final_1 = int(input("Ogrenci Final giriniz: "))
                VeriTabani[ogrenciNo]["Final"] = Final_1
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
            else:
                print("Hatali Giris yaptiniz!")
                input("Guncelleme menusune donmek icin ENTER'e basiniz..")
        else:
            print("Ogrenci numarasina ait kayit bulunamadi !")
            input("Guncelleme menusune donmek icin ENTER'e basiniz..")

        not_toplam = Odev_1 + Odev_2 + Kisa_Sinav_1 + Kisa_Sinav_2 + Proje_1 + Vize_1 + Final_1
        not_ortalamasi = not_toplam * 0.05

        sozluk = {"okulNo": okulNo, "ad": ad, "soyad": soyad, "Ödev 1": Odev_1, "Ödev 2": Odev_2, "Kısa Sınav 1": Kisa_Sinav_1, "Kısa Sınav 2": Kisa_Sinav_2, "Proje 1": Proje_1, "Vize": Vize_1,"Final": Final_1, "Not Ortalaması": not_ortalamasi}
        VeriTabani[okulNo] = sozluk

        if (not_ortalamasi >= 90 and not_ortalamasi <= 100):
            sozluk["Notu"] = "AA"
        if (not_ortalamasi >= 80 and not_ortalamasi <= 89):
            sozluk["Notu"] = "BA"
        if (not_ortalamasi >= 70 and not_ortalamasi <= 79):
            sozluk["Notu"] = "BB"
        if (not_ortalamasi >= 60 and not_ortalamasi <= 69):
            sozluk["Notu"] = "CB"
        if (not_ortalamasi >= 50 and not_ortalamasi <= 59):
            sozluk["Notu"] = "CC"
        if (not_ortalamasi >= 40 and not_ortalamasi <= 49):
            sozluk["Notu"] = "DC"
        if (not_ortalamasi >= 20 and not_ortalamasi <= 39):
            sozluk["Notu"] = "DD"
        if (not_ortalamasi >= 00 and not_ortalamasi <= 19):
            sozluk["Notu"] = "FF"


def ekran(): #Yapacağımız işlemleri kullanıcağımız fonksiyon
    while True:
        print("Not Hesaplama Uygulamasına Hoş Geldiniz")
        print(13*" * ")
        print("Seçimleriniz.. \nÖğrenci Notlarını Ekle (Ekle) \nÖğrencileri Görüntüle (Gör) \nÖğrenci Kayıt Silme (Sil) \nÖğrenci Notu Güncelleme (Güncel) \nÇıkış (Q-q)")
        secim = str(input("İşleminiz: "))
        if secim == "Ekle":
            ogrenciNotlariniEkle()
            input("Ana menu'ye donmek icin ENTER'e basiniz..")
        elif secim == "Gör":
            ogrencileriListele()
            input("Ana menu'ye donmek icin ENTER'e basiniz..")
        elif secim == "Sil":
            OgrenciNotlariniSil()
            input("Ana menu'ye donmek icin ENTER'e basiniz..")
        elif secim == "Güncel":
            notGuncelleme()
        elif secim == "q" or secim == "Q":
            quit()
        else:
            print("Hatali Giris yaptiniz!")
            input("Ana menu'ye donmek icin ENTER'e basiniz..")
ekran()