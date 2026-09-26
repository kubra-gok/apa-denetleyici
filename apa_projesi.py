import re
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
    if "doi" in metin.lower() and "https://doi.org/10." not in metin:
        print("❌ HATA: DOI eski formatta, https://doi.org/... şeklinde olmalı")
        print("   Kaynak:", metin[:50], "...")
        print()   