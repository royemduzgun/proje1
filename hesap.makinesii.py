from tkinter import*

def yaz(x):
    s=len(giriş.get())
    giriş.insert(s,str(x))

hesap=7
s1=0

def işlemelr(x):
    global hesap
    hesap(x)
    global s1
    s1=float(giriş.get())
    print(s1)
    giriş.delete(0,"end")

s2=0
def hesapla():
    global s2
    s2=float(giriş.get())
    print(s2)
    global hesap
    sonuç=0
    if(hesap==0):sonuç=s1+s2
    elif(hesap==1):sonuç=s1-s2
    elif(hesap==2):sonuç=s1*s2
    elif(hesap==3):sonuç=s1/s2
    giriş.delete(0,"end")
    giriş.insert(0,str(sonuç))

pencere=Tk()
pencere.title("HESAP MAKİNESİ")
pencere.geometry("500x500")
giriş=Entry(font="Verdana 14 bold",width=20,justify=RIGHT)
giriş.place(x=80,y=20)
b=[]
for i in range(1,10):
    b.append(Button(text=str(1),font="Verdana 14 bold",width=4,command=lambda x=i:yaz(x)))
sayaç=0
for i in range(0,3):
    for j in range(0,3):
        b[sayaç].place(x=80+j*70,y=80+i*70)
        sayaç+=1
işlem=[]
for i in range(0,4):
    işlem.append(Button(fg="RED",bg="GRAY",font="Verdana 14 bold",width=4,command=lambda x=i:işlemler(x)))
işlem[0]["text"]="+"
işlem[1]["text"]="-"
işlem[2]["text"]="*"
işlem[3]["text"]="/"
for i in range(0,4):
    işlem[i].place(x=300,y=80+50*i)

sıfb=Button(text=0,font="Verdana 14 bold",width=4,command=lambda x=0:yaz(x))
sıfb.place(x=80,y=200)
noktb=Button(text=".",font="Verdana 14 bold",width=4,command=lambda x=".":yaz(x))
noktb.place(x=220,y=280)
eşittrb=Button(text="=",fg="RED",bg="GRAY",font="Verdana 14 bold",width=4,command=hesapla)
eşittrb.place(x=300,y=200)

pencere.mainloop()
            
            

            

    
                                                            
 

                          
