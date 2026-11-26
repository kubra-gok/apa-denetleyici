# Benzer Araçlar: Karşılaştırma Notları

Test dosyası: `deneme_kaynakca.docx` (8 kaynak, bilinen 6 hata)
Test tarihi: 25 Kasım 2026

## 1. Kaynakça Doğrula (kaynakcadogrula.com)

**Odak:** "Kaynak gerçekten var mı?" Kaynakları akademik veritabanlarında arayıp eşleşme puanı veriyor.

**Sonuç:** "Bütün kaynaklar sorunsuz." (5 kaynak listelendi, dosyada 8 vardı)

**Kaçırdığı biçim hataları:**
- Kahneman & Tversky: yıl parantezsiz (`A. 1979.`) → "Sorun yok" dedi
- Kahneman (2011): kitap adı italik değil → fark etmedi

**Benim programımdan farkı:**
Bu araç kaynağın **varlığını** doğruluyor, **APA biçim kurallarına** (yıl parantezi, italik, font) bakmıyor.
Benim programım aynı dosyada 6 biçim hatası buluyor ve DOI'yi de Crossref ile doğruluyor.

| Kontrol | Kaynakça Doğrula | Benim programım |
|---|---|---|
| Kaynak gerçek mi? (DOI) | ✅ | ✅ |
| Yıl parantezi | ❌ kaçırdı | ✅ |
| İtalik | ❌ kaçırdı | ✅ |
| Font tutarlılığı | ? | ✅ |
| "&" kullanımı | ? | ✅ |
| Eski DOI formatı | ? | ✅ |

**Açık soru:** 8 kaynaktan neden sadece 5'ini listeledi?

## 2. Recite (reciteworks.com)

**Odak:** Metin içi atıflar ile kaynakçanın eşleşmesi.
Tam makale istiyor (metin + kaynakça). Sadece kaynakçadan oluşan bir dosyayla asıl işini yapamıyor.

**Test:** Kullanmak için Google hesabıyla giriş gerekiyor. `deneme_kaynakca.docx` yüklendiğinde hata verdi:
"ERROR: The text you uploaded contained no detectable reference section."
Muhtemel sebep: Başlık Türkçe ("Kaynakça"). Recite'ın SSS'sine göre APA için başlık tam olarak "References" olmalı, başka dil kabul edilmiyor.
→ **Türkçe başlıklı belgeleri tanımıyor.**

**İkinci test:** `deneme_kaynakca_recite.docx` (başlık "References", üstüne atıflı kısa bir metin eklendi).
Metne 2 tuzak kondu: Turing (1952) (kaynakçada 1950) ve Knuth (1997) (kaynakçada yok).

**Metin içi atıflar:** Tuzakların ikisini de yakaladı ✅
- Turing: "Year mismatch"
- Knuth: "No references for author(s) or year"
- Bonus: Çoklu atıfın alfabetik sırada olmadığını da uyardı

**Kaynakça biçim hataları: 6'dan 2'sini buldu**

| Hata | Recite | Benim programım |
|---|---|---|
| Yıl parantezsiz (Kahneman & Tversky) | ✅ | ✅ |
| "ve" yerine "&" (Rivest) | ✅ | ✅ |
| Kitap adı italik değil (Kahneman 2011) | ❌ | ✅ |
| Dergi adı italik değil (Shannon) | ❌ | ✅ |
| Font tutarsızlığı (Singh, Arial) | ❌ | ✅ |
| Eski DOI formatı (Turing, `doi:`) | ❌ | ✅ |
| DOI gerçekten var mı? (Crossref) | ❌ Ücretsiz planda yok | ✅ |
| Metin içi atıf ↔ kaynakça eşleştirme | ✅ | ❌ |

**Benim programımdan farkı:** İki araç birbirini tamamlıyor.
Recite metin içi atıf eşleştirmede güçlü. Benim programım biçim kurallarında (italik, font, DOI formatı) ve ücretsiz DOI doğrulamada daha güçlü.
Atıf eşleştirme "gelecek çalışmalar"a eklenebilir.

## 3. Edifix (edifix.com)

**Odak:** Yayınevleri için profesyonel kaynakça biçimlendirme ve DOI düzeltme. Ücretli (ilk 25 kaynak ücretsiz).

**Test:** Ücretsiz deneme hesabıyla (25 kaynak hakkı, tek seferde en fazla 10). 8 kaynak düz metin olarak yapıştırıldı, APA 7 + Crossref/PubMed seçildi. Yaklaşık 2-3 dakika sürdü.
Fiyat: En küçük paket 250 kaynak için 39,95 dolar.

**Sonuç: En güçlü rakip.** Hataları bulmakla kalmıyor, **düzeltip** "izlenen değişiklikler" gibi gösteriyor.

| Hata | Edifix | Benim programım |
|---|---|---|
| Yıl parantezsiz (Kahneman & Tversky) | ✅ düzeltti | ✅ buldu |
| "ve" yerine "&" (Rivest) | ✅ düzeltti, ama "ve"yi tanımadığı için kafası karıştı ("Unrecognized text", yazar listesini elle kontrol et uyarısı) | ✅ buldu |
| Dergi adı italik değil (Shannon) | ✅ italik yaptı ("The" ekledi) | ✅ buldu |
| Kitap adı italik değil (Kahneman 2011) | ✅ çıktıda italik | ✅ buldu |
| Eski DOI formatı (Turing) | ✅ düzeltti | ✅ buldu |
| Font tutarsızlığı (Singh) | ❌ test edilemez, düz metinle çalışıyor | ✅ |
| DOI gerçek mi? | ✅ (8'den 6'sı Crossref'e bağlandı) | ✅ |
| Ekstra | Erratum uyarısı (LeCun), Crossref'e göre cilt düzeltme önerisi (Turing: 59 → LIX), yağmacı dergi kontrolü | ❌ |

**Benim programımdan farkı:**
- Edifix daha kapsamlı ve otomatik düzeltme yapıyor. Benim programım şu an sadece buluyor.
- Edifix ücretli ve web tabanlı: Kaynaklar kopyalanıp siteye yapıştırılıyor, sonuç tekrar Word'e kopyalanıyor. Benim programım Word dosyasını doğrudan okuyor, bilgisayardan çıkarmıyor.
- Edifix düz metinle çalıştığı için Word'deki font tutarsızlığını göremiyor.
- Türkçe "ve" bağlacını tanımıyor.

## Genel gözlemler

- **Gizlilik:** Web tabanlı araçlarda metin üçüncü taraf sunucusuna yükleniyor. Benim programım dosyayı kendi bilgisayarında okuyor, dışarıya sadece DOI numarasını gönderiyor.
- **Dil:** Türkçe kaynaklarda APA "&" yerine "ve" kullanıyor. Benim programım şu an İngilizce kaynaklara göre tasarlandı.
