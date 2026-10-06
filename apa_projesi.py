import re
import requests
from docx import Document

# Word dosyasını aç
belge = Document("deneme_kaynakca.docx")

# Her paragrafı tek tek gez
for paragraf in belge.paragraphs:
    metin = paragraf.text.strip()

    # Boş satırları ve başlığı atla
    if metin == "" or metin == "Kaynakça":
        continue

    # KURAL 1: Yıl parantez içinde ve ardından nokta olmalı. Örnek: (2020).
    if not re.search(r"\(\d{4}\)\.", metin):
        print("❌ HATA: Yıl (2020). şeklinde yazılmamış")
        print("   Kaynak:", metin[:50], "...")
        print()
        # KURAL 2: Son yazardan önce "ve" / "and" değil "&" kullanılmalı
    # Sadece yazar kısmına bakıyoruz: ilk parantezden öncesi
    yazarlar = metin.split("(")[0]
    if " ve " in yazarlar or " and " in yazarlar:
        print("❌ HATA: Yazarlar arasında 've' yerine '&' kullanılmalı")
        print("   Kaynak:", metin[:50], "...")
        print()
        # KURAL 3: Her kaynakta dergi ya da kitap adı italik olmalı
    # Paragraftaki parçalardan (run) en az biri italik mi, ona bakıyoruz
    italik_var = any(parca.italic for parca in paragraf.runs)
    if not italik_var:
        print("❌ HATA: Hiç italik yok (dergi ya da kitap adı italik olmalı)")
        print("   Kaynak:", metin[:50], "...")
        print()
        # KURAL 4: DOI varsa https://doi.org/ ile başlamalı (eski "doi:" formatı yanlış)
    if ("doi: 10" in metin.lower() or "doi:10" in metin.lower()) and "https://doi.org/10." not in metin:
        print("❌ HATA: DOI eski formatta, https://doi.org/... şeklinde olmalı")
        print("   Kaynak:", metin[:50], "...")
        print()
        # KURAL 5: Font tutarlılığını kontrol et (tüm paragraflar aynı fontta olmalı)
        # KURAL 5: Font tutarlılığı (her parça Times New Roman olmalı)
    yanlis_font_var = False
    for parca in paragraf.runs:
        if parca.font.name is not None and parca.font.name != "Times New Roman":
            yanlis_font_var = True
    if yanlis_font_var:
        print("❌ HATA: Font tutarlı değil (Times New Roman olmalı)")
        print("   Kaynak:", metin[:50], "...")
        print()
          # KURAL 6: DOI doğrulama (Crossref'e sorarak)
    bulunan = re.search(r"10\.\d{4,9}/\S+", metin)
    if bulunan:
        doi = bulunan.group()
        # Sondaki nokta hem APA hatası hem de Crossref'i şaşırtır
        if doi.endswith("."):
            print("❌ HATA: DOI'nin sonunda nokta olmamalı")
            print("   Kaynak:", metin[:50], "...")
            print()
            doi = doi.rstrip(".")

        try:
            cevap = requests.get("https://api.crossref.org/works/" + doi, timeout=10)
        except requests.exceptions.RequestException:
            print("⚠️  UYARI: Crossref'e ulaşılamadı, bu DOI kontrol edilemedi")
            print("   Kaynak:", metin[:50], "...")
            print()
        else:
            if cevap.status_code == 404:
                print("❌ HATA: Bu DOI Crossref'te yok (hatalı ya da uydurma olabilir)")
                print("   Kaynak:", metin[:50], "...")
                print()
            elif cevap.status_code == 200:
                basliklar = cevap.json()["message"].get("title", [])
                if basliklar:
                    gercek_baslik = basliklar[0]
                    # Crossref'teki başlığın kelimelerinin kaçı kaynakçada geçiyor?
                    kelimeler = re.findall(r"\w+", gercek_baslik.lower())
                    eslesen = 0
                    for kelime in kelimeler:
                        if kelime in metin.lower():
                            eslesen = eslesen + 1
                    if eslesen / len(kelimeler) < 0.7:
                        print("❌ HATA: DOI başka bir makaleye ait olabilir")
                        print("   Kaynak:", metin[:50], "...")
                        print("   Crossref'teki başlık:", gercek_baslik)
                        print()  
