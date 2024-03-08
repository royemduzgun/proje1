import tkinter as tk
from time import strftime
import random

class RenkliSaatUygulamasi:
    def __init__(self, master):
        self.master = master
        master.title("Renkli Saat Uygulaması")
        master.geometry('300x150')

        self.saat_etiketi = tk.Label(master, font=('calibri', 40, 'bold'), background='white', foreground='black')
        self.saat_etiketi.pack(anchor='center')

        self.zaman_guncelle_id = None  # Saatı güncelleme işlemi için bir ID sakla

        self.zaman_guncelle()

        self.renk_dugme = tk.Button(master, text="Renk Değiştir", command=self.renk_degistir)
        self.renk_dugme.pack()

        self.basla_durdur_dugme = tk.Button(master, text="Saatı Durdur/Başlat", command=self.saat_duraklat_baslat)
        self.basla_durdur_dugme.pack()

    def zaman_guncelle(self):
        self.string = strftime('%H:%M:%S %p')
        self.saat_etiketi.config(text=self.string)
        self.zaman_guncelle_id = self.saat_etiketi.after(1000, self.zaman_guncelle)

    def renk_degistir(self):
        renk = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.saat_etiketi.config(foreground=renk)

    def saat_duraklat_baslat(self):
        if self.zaman_guncelle_id is not None:
            self.saat_etiketi.after_cancel(self.zaman_guncelle_id)
            self.zaman_guncelle_id = None
        else:
            self.zaman_guncelle()

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = RenkliSaatUygulamasi(root)
    root.mainloop()

