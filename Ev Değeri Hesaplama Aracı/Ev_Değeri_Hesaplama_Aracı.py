# Yapılan matematiksel işlemleri daha iyi anlamak için Özgür Demirtaş'ın videosunu izlemenizi öneririm.
# I suggest to you watch the Özgür DEmirtaş's video for better understand the mathematical operations performed.
# First video / Birinci video : https://www.youtube.com/watch?v=R1MJzPrVZmY
# Second video / İkinci Video : https://www.youtube.com/watch?v=GfVRLGHeE_Q


x = int(input("Evinizi Kaç Yıl Sonra Satacaksınız? (TAHMİNİ) : "))
z = int(input("Bu süreden Sonra Evinizi Ne Kadara Satacaksınız? (TAHMİNİ) ? : "))
y = int(input("Kiraya Verecek Olsanız Aylık Ne Kadar Kira Alırsınız? : "))
k = float(input("Faiz Oranını (0.'faiz') Şeklinde Giriniz (Önerilen = %15 yani 0.15) : "))

yıllık_kira_geliri = y*12

# Türkiye'de 450 Türk Lirası üstünde kira alan herkes "Kira gelir vergisi" vermek zorundadır.
# Kira gelir vergisi kişiden kişiye değişiklik gösterdiği için bu veriyi kullanıcıdan almak gerekir.

if (y > 450):
    l = float(input("Kira Gelir Verginiz Yıllık % Kaç? [BİLMİYORSANIZ '15' ÖNERİLİR] : "))
    yıllık_kira_vergisi = (yıllık_kira_geliri/100)*l

else:
    print("Kira Vergisi Vermeyeceğiniz İçin Vergilendirme İptal Edilmiştir .")
    yıllık_kira_vergisi = (yıllık_kira_geliri/100)*0


bir_yıllık_net_kira_geliri = yıllık_kira_geliri - yıllık_kira_vergisi

satış_parasının_değeri = z/(1+k)**x

toplam_kira_değeri = 0

for üssü_değeri in range(1,x+1):
    para_değerinin_yıllara_göre_düşmesi = bir_yıllık_net_kira_geliri/(1+k)**üssü_değeri
    toplam_kira_değeri += para_değerinin_yıllara_göre_düşmesi
    

ev_değeri = toplam_kira_değeri + satış_parasının_değeri
print("EVİN DEĞERİ : " , ev_değeri)