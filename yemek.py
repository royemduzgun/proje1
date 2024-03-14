class YemekTarifiKitapcigi:
    def __init__(self):
        self.tarifler = {}

    def tarif_ekle(self, yemek_adi, malzemeler, tarif):
        """Yeni bir tarif ekler"""
        self.tarifler[yemek_adi] = {"malzemeler": malzemeler, "tarif": tarif}
        print(f"{yemek_adi} tarifi eklendi.")

    def tarif_goruntule(self, yemek_adi):
        """Belirli bir tarifi görüntüler"""
        if yemek_adi in self.tarifler:
            print(f"{yemek_adi} Tarifi:")
            print("Malzemeler:", self.tarifler[yemek_adi]["malzemeler"])
            print("Tarif:", self.tarifler[yemek_adi]["tarif"])
        else:
            print("Bu isimde bir tarif bulunamadı.")

    def tum_tarifleri_listele(self):
        """Tüm tarifleri listeler"""
        print("Yemek Tarifi Kitapçığı")
        for yemek_adi, tarif in self.tarifler.items():
            print(f"{yemek_adi}: {tarif['tarif']}")

if __name__ == "__main__":
    kitapcik = YemekTarifiKitapcigi()

    while True:
        print("\nYemek Tarifi Kitapçığına Hoş Geldiniz!")
        print("1. Tarif Ekle")
        print("2. Tarif Görüntüle")
        print("3. Tüm Tarifleri Listele")
        print("4. Çıkış")

        secim = input("Lütfen bir seçenek seçin: ")

        if secim == "1":
            yemek_adi = input("Yemek adı: ")
            malzemeler = input("Malzemeler (virgülle ayırarak): ").split(",")
            tarif = input("Tarif: ")
            kitapcik.tarif_ekle(yemek_adi, malzemeler, tarif)
        elif secim == "2":
            yemek_adi = input("Görüntülemek istediğiniz yemek adı: ")
            kitapcik.tarif_goruntule(yemek_adi)
        elif secim == "3":
            kitapcik.tum_tarifleri_listele()
        elif secim == "4":
            print("Yemek Tarifi Kitapçığı'ndan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
