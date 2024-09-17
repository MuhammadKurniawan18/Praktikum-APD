NAMA = "Muhammad Kurniawan"
NIM = "2409106091" 
HargaGula = 21000


DiskonGulaku = 0.07
DiskonManisKita = 0.11
DiskonGunungMadu = 0.13


DiskonGulaku = HargaGula * DiskonGulaku
DiskonManisKita = HargaGula * DiskonManisKita
DiskonGunungMadu = HargaGula * DiskonGunungMadu

HargaSetelahDiskonGulaku = HargaGula - DiskonGulaku
HargaSetelahDiskonManiskita = HargaGula - DiskonManisKita
HargaSetelahDiskonGunungMadu = HargaGula - DiskonGunungMadu

print(f"{NAMA} dengan NIM {NIM} ingin membeli beras seharga Rp {HargaGula}")
print(f"jika dia membeli Gulaku ia harus membayar {HargaSetelahDiskonGulaku} setelah mendapat diskon 7%")
print(f"jika dia membeli Manis Kita ia harus membayar {HargaSetelahDiskonManiskita} setelah mendapat diskon 11%")
print(f"jika dia membeli Gunung Madu ia harus membayar {HargaSetelahDiskonGunungMadu} setelah mendapat diskon 13%")