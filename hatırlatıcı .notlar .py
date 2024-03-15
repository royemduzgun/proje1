import json
import os

Notlar dosya_adı
Notlar ="notlar.json"

def notlari_yukle():
    if os.path.exists(Notlar):
        with open (Notlar,"r")as file:
            return json.load(file)

    else:
        return{}

    
def notlari_kaydet(notlar):
    with open(Notlar,"w")as file:
        json.dump(notlar,file)

def not_ekle():
    baslik=input("Not başlığı:")
    icerik=input("Not içeriği:")

    notlar[baslik]=icerik
    notlari_kaydet(notlar)
    print("Not başarıyla eklendi.")

def notlari_listele():
    print("Notlarınız:")
    for baslik,icerik in notlar.items():
        print(f"\n{baslik}:\n{icerik}")

def not_sil():
    baslik=input("Silinecek notun baslığını girin:")
    if baslik in notlar:
        del notlar[baslik]
        notlari_kaydet(notlar)
        print("Not başarıyla silindi.")
    else:
        print("Belirtilen başlıkta bir not bulunmadı.")

if __name__=="__main__":
    notlar=notlari_yukle()

    while True:
        print("\nHoş Geldiniz!")
        print("1. Not Ekle")
        print("2. Notları Listele")
        print("3. Not Sil")
        print("4. Çıkış")

        secim = input("Lütfen bir seçenek seçin: ")


        if secim == "1":
            not_ekle()
        elif secim == "2":
            notlari_listele()
        elif secim == "3":
            not_sil()
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


       
        
