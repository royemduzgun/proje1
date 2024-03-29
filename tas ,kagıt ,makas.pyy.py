import random

def oyun():
    secenekler=['tas','kagıt','makas']
    bilgisayar_secimi =random.choice(secenekler)
    kullanıcı_secimi =input("tas mı , kagıt mı,makas mı?").lower()

    if kullanıcı_secimi not in  secenekler:
        print("geceersiz secim.lütfen 'tas','kagıt'veya 'makas'seçin.")
        return

    print(f"bilgisayarın secimi:{bilgisayar_secimi}")
    print(f"sizden: {kullanıcı_secimi}")


    if bilgisayar_secimi==kullanıcı_secimi:
        print("berabere!")
    elif (bilgisayar_secimi == 'taş' and kullanici_secimi == 'makas') or \
         (bilgisayar_secimi == 'makas' and kullanici_secimi == 'kağıt') or \
         (bilgisayar_secimi == 'kağıt' and kullanici_secimi == 'taş'):
        print("bilgisayar kazandı!")
    else:
        print("tebrikler! siz kazandınız!")

while True:
    oyun()
    devam=input("yeniden oynamak istiyor musunuz? (e/h:").lower()
    if devam !='e':
        break
