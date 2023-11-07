from datetime import datetime

dogum_gunu = input("Doğum gününüzü (GG/AA/YYYY) formatında girin: ")

dogum_tarihi = datetime.strptime(dogum_gunu, "%d/%m/%Y")

bugun = datetime.now()

yas = bugun.year - dogum_tarihi.year

if bugun.month < dogum_tarihi.month or (bugun.month == dogum_tarihi.month and bugun.day < dogum_tarihi.day):
    yas -= 1

saniye = (bugun - dogum_tarihi).total_seconds()
deqiqe = saniye / 60
saat = deqiqe / 60
gun = saat / 24
ay = yas * 12

print(f"Siz hayatta {int(saniye):,} saniye, {int(deqiqe):,} deqiqe, {int(saat):,} saat, {int(gun):,} gün ve {int(ay):,} aydır varsiniz ve {yas} yaşınız var.")
