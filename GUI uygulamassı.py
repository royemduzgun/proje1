import tkinter as tk
import random


pencere = tk.Tk()
pencere.title("Dosya Maker")
pencere.geometry("700x300")
pencere.resizable(width="False", height="False")

frame = tk.Frame(pencere)
frame.pack()

giriş = tk.Label(frame, text="kayıtsız", bg="black", fg="white", font="Korataki 11")
giriş.pack(side=tk.LEFT)

giriş1 = tk.Label(frame, text="0", bg="black", fg="white", font="Korataki 11")
giriş1.pack(side=tk.LEFT)

def kayıt():
    giriş.config(text="User", fg="red")
    liste=[]
    for i in range(1):
        while len(liste) != 1:
            a = random.randint(1, 100)
            if a not in liste:
                liste.append(a)
    giriş1["text"] = liste
    giriş1.config(fg="red")


by = tk.Label(pencere, text="Yapan kişi=Royem", fg="black", font="Korataki 11")
by.place(relx=1.0, rely=0.0, anchor='ne')

def Full():
    pencere.state("zoomed")

yazı = tk.Label(pencere, text="DOSYA MAKER", bg="orange", fg="red", font="Algerian 22")
yazı.pack()

def oluştur():
    dosya = open("deneme.txt", "w")
    dosya.close()
    yazı2.config(text="Dosya oluşturuldu")

buton = tk.Button(pencere, text="Çıkış", command=pencere.quit, bg="red")
buton.pack()

buton2 = tk.Button(pencere, text="Dosya oluştur", command=oluştur, bg="red", fg="black", width="20", height="2")
buton2.pack()

yazı2 = tk.Label(pencere, text="Not: dosya deneme.txt adı ile oluşur")
yazı2.pack()

buton3 = tk.Button(pencere, text="Giriş", bg="red", fg="black", width="4", height="1", command=kayıt)
buton3.pack()

Ekranı = tk.Button(pencere, text="Ekranı fulle", bg="red", fg="black", width="10", height="2", command=Full)
Ekranı.pack(side=tk.BOTTOM)

pencere.mainloop()
