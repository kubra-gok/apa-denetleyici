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