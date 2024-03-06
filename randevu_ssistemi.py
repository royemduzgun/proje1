import tkinter as tk
from tkinter import messagebox




class RandevuSistemi:
    def __init__(self, master):
        self.master = master
        self.master.title("Hastane Randevu Sistemi")

        self.label_hosgeldiniz = tk.Label(master, text="Hastanemize Hoş Geldiniz", font=("Arial", 16, "bold"))
        self.label_hosgeldiniz.pack()

    
        self.label_doktor = tk.Label(master, text="Doktorun adını giriniz:")
        self.label_doktor.pack()
        self.entry_doktor = tk.Entry(master)
        self.entry_doktor.pack()

        self.label_tarih = tk.Label(master, text="Tarih giriniz (örn. 2024-03-06):")
        self.label_tarih.pack()
        self.entry_tarih = tk.Entry(master)
        self.entry_tarih.pack()

        self.label_saat = tk.Label(master, text="Saat giriniz (örn. 14:30):")
        self.label_saat.pack()
        self.entry_saat = tk.Entry(master)
        self.entry_saat.pack()

        self.button_randevu_al = tk.Button(master, text="Randevu Al", command=self.randevu_al)
        self.button_randevu_al.pack()

        self.button_cikis = tk.Button(master, text="Çıkış", command=master.quit)
        self.button_cikis.pack()

    def randevu_al(self):
        doktor = self.entry_doktor.get()
        tarih = self.entry_tarih.get()
        saat = self.entry_saat.get()

        # Randevu alma işlemleri burada gerçekleştirilecek, şu anlık sadece bir mesaj kutusu ile bilgi veriyoruz
        messagebox.showinfo("Bilgi", f"{doktor} adlı doktordan {tarih} tarihinde saat {saat} için randevu alındı.")



root = tk.Tk()
randevu_sistemi = RandevuSistemi(root)
root.mainloop()
