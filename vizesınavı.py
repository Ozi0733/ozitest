







import tkinter as tk

sorular = [
    ("En sevdiğim renk nedir?", "siyah", "Doğru cevap siyah, çünkü siyah hem sade hem karizmatiktir."),
    ("En sevdiğim yemek nedir?", "et", "Etli yemekleri seviyorum, hele güzel pişmiş bir kebap gibisi yok."),
    ("En büyük takıntım nedir?", "sakız çiğnenmesi", "Sakız sesi beni deli eder, en büyük takıntım bu."),
    ("En büyük hobim nedir?", "yeni yerler keşfetmek", "Yeni yerler gezmek, görmek beni her zaman mutlu eder."),
    ("En sevmediğim huyum nedir?", "sabahları suratsız olmak", "Sabahları biraz asık suratlı olabiliyorum, kabul."),
    ("Şehnaz'ın plakası nedir?", "06 cod 796", "06 COD 796 – ezberimde bile artık bu plaka."),
    ("Ben en çok neyi özledim?", "sareye sarılmayı", "Sare'ye sarılmayı özlemek başka bir duygu..."),
    ("Balımla en sevdiğim aktivite nedir?", "lazer ile balımı delirtmek", "Lazerle oynamak ve balımı çıldırtmak en keyifli anlardan."),
    ("Seni bana hangi şarkı hatırlatıyor olabilir?", "deva bize sevişler", "Bazı şarkılar vardır, kişileri hatırlatır. Bu da öyle."),
    ("En sevdiğim şarkı nedir?", "soldier of fortune", "Deep Purple'ın efsane şarkısı Soldier of Fortune!")
]

puan = 0
soru_index = 0
kalan_sure = 25
zamanlayici_id = None

def zaman_sayaci():
    global kalan_sure, zamanlayici_id
    if kalan_sure > 0:
        kalan_sure -= 1
        sure_label.config(text=f"Kalan süre: {kalan_sure} sn")
        zamanlayici_id = pencere.after(1000, zaman_sayaci)
    else:
        cevapla_otomatik()

def soruyu_goster():
    global soru_index, kalan_sure, zamanlayici_id
    if soru_index < len(sorular):
        soru_label.config(text=sorular[soru_index][0])
        cevap_entry.delete(0, tk.END)
        sonuc_label.config(text="")
        adamsin_label.config(text="")  # Yeni alanı sıfırla
        kalan_sure = 25
        sure_label.config(text=f"Kalan süre: {kalan_sure} sn")
        zaman_sayaci()
    else:
        soru_label.config(text=f"Test bitti! Toplam puanınız: {puan}/100")
        cevap_entry.pack_forget()
        cevapla_buton.pack_forget()
        sure_label.pack_forget()
        sonuc_label.config(text="")
        adamsin_label.config(text="")

def cevabi_kontrol_et():
    global puan, soru_index, zamanlayici_id
    pencere.after_cancel(zamanlayici_id)
    kullanici_cevap = cevap_entry.get().strip().lower()
    dogru_cevap = sorular[soru_index][1]
    yorum = sorular[soru_index][2]
    
    if dogru_cevap in kullanici_cevap:
        puan += 10
        sonuc_label.config(text="✅ Doğru cevap! +10 puan")
        adamsin_label.config(text="🔥 ADAMSIN! 🔥")
    else:
        sonuc_label.config(text=f"😢 Yanlış cevap!\n{yorum}")
        adamsin_label.config(text="")
    
    soru_index += 1
    pencere.after(3000, soruyu_goster)

def cevapla_otomatik():
    global soru_index
    yorum = sorular[soru_index][2]
    sonuc_label.config(text=f"😢 Süre doldu!\n{yorum}")
    adamsin_label.config(text="")
    soru_index += 1
    pencere.after(3000, soruyu_goster)

# GUI Kurulumu
pencere = tk.Tk()
pencere.title("Oğuzhan'ın Kişisel Testi")
pencere.geometry("500x360")

soru_label = tk.Label(pencere, text="", font=("Arial", 12), wraplength=400)
soru_label.pack(pady=20)

sure_label = tk.Label(pencere, text="", font=("Arial", 10), fg="red")
sure_label.pack()

cevap_entry = tk.Entry(pencere, width=50)
cevap_entry.pack()

cevapla_buton = tk.Button(pencere, text="Cevapla", command=cevabi_kontrol_et)
cevapla_buton.pack(pady=10)

sonuc_label = tk.Label(pencere, text="", font=("Arial", 10), fg="blue", wraplength=450)
sonuc_label.pack()

adamsin_label = tk.Label(pencere, text="", font=("Arial", 12, "bold"), fg="green")
adamsin_label.pack(pady=5)

soruyu_goster()
pencere.mainloop()









