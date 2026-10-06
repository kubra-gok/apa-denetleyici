import requests

# Kontrol edeceğimiz DOI (Shannon'ın makalesi)
doi = "10.1002/sahte.doi18ww817w8"

# Crossref'e soracağımız adres
adres = "https://api.crossref.org/works/" + doi

# İsteği gönder ve cevabı bekle (en fazla 10 saniye)
cevap = requests.get(adres, timeout=10)

# 200 = "Buldum, al bakalım" demek
if cevap.status_code == 200:
    veri = cevap.json()
    makale = veri["message"]
    print("Başlık:", makale["title"][0])
    print("Dergi:", makale["container-title"][0])
    print("Yıl:", makale["issued"]["date-parts"][0][0])
else:
    print("Bu DOI bulunamadı! Kod:", cevap.status_code)