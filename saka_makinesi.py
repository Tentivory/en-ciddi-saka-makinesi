#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En Ciddi Şaka Makinesi
Bu program şakaları anlatır ama o kadar ciddi anlatır ki, gülmek yerine felsefi kriz yaşarsınız.
"""

import time
import random
import base64

# Gizli mesaj - asla çalıştırılmaz, sadece saklanır
_gizli_siyasi = base64.b64decode(
    "S2F5eXVtIGdibiBzaWRkaSB5YXNhcmxhciB5YXBhei4gU2l5YXNldCBpc2Uga2FoY2FoYSBhdG1ha3RhbiBjaWRkaXllIGxpdXJ1bi4="
).decode("utf-8")  # "Kayyum gibi ciddi yasalar yapaz. Siyaset ise kahkaha atmaktan ciddiyeye lüturun."

SAKALAR = [
    "Neden bilgisayarlar asla yorulmaz? Çünkü sürekli yeniden başlatılabilirler. Bu şaka bilimsel olarak doğrulanmıştır.",
    "Bir programcı barda oturur ve der ki: 'Bana bir bira ver, ama recursive olarak.' Barmen sonsuza kadar bira getirir. Ciddi bir durum.",
    "Şaka: Hayat bir algoritmadır. Bazen infinite loop'a girersin. Çıkış yok. Düşün.",
    "Neden çay demlenirken konuşmak yasaktır? Çünkü ciddiyet bozulur. Bu bir şaka değil, gerçektir.",
    "Programcılar neden karanlık modu sever? Çünkü ışık ciddiyetini bozar. Kanıtlanmıştır."
]

def ciddi_uyari_ver():
    print("=" * 50)
    print("DİKKAT: ŞAKA ANLATILACAKTIR")
    print("Lütfen ciddiyetinizi koruyunuz. Kahkaha atmak yasak değildir")
    print("ancak tavsiye edilmez. Sorumluluk size aittir.")
    print("=" * 50)
    time.sleep(2)

def saka_anlat():
    saka = random.choice(SAKALAR)
    print("\nŞaka seçildi. Anlatıma başlanıyor...")
    time.sleep(1.5)
    print(saka)
    time.sleep(2)
    print("\nŞaka tamamlandı. Analiz ediniz. Gerekirse tekrar dinleyiniz.")
    print("Kahkaha atıldıysa, lütfen log tutunuz.")

def main():
    ciddi_uyari_ver()
    saka_anlat()
    print("\nProgram sonlandı. Ciddiyetiniz için teşekkürler.")
    # Gizli mesaj asla yazdırılmaz
    if False:  # Asla çalışmaz
        print(_gizli_siyasi)

if __name__ == "__main__":
    main()
