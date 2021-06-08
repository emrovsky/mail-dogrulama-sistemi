  
from smtplib import SMTP
import random
a = random.randint(10000,99999)

dosya = open("bilgiler.txt","r",encoding="utf-8")
hesap = (dosya.readline())
sifre = (dosya.readline())

gonderilecekadres = input("Sisteme kayıt olmak için mail adresinizi giriniz size bir kod yollayacağız! : ")
try:
    # Mail Mesaj Bilgisi 
    konu = "Emrovsky otomasyon sistemi"
    mesaj = ("Emrovsky otomasyon sistemi için kodunuz"+ "  :" + str(a))
    icerik = "Subject: {0}\n\n{1}".format(konu,mesaj)

    # Hesap Bilgileri 
    mailadresi = hesap
    sifre = sifre




    # Kime Gönderilecek Bilgisi
    sendTo = gonderilecekadres

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(mailadresi,sifre)
    mail.sendmail(mailadresi, sendTo, icerik.encode("utf-8"))
    print("Kodunuz başarıyla gönderildi!")
    kod = int(input("Lütfen gönderdiğimiz kodu giriniz : "))
    if kod == a:
        print("Sisteme başarıyla kayıt oldunuz!")
        print("Giriş ekranı :D")
    else:
        print("Kod hatalı yazılımı baştan çalıştırıp yeni bir kod alınız :)")

except Exception as e:
    print("Hata Oluştu!\n {0}".format(e))