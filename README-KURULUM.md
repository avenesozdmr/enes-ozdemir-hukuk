# Av. Enes ÖZDEMİR — Makale yönetimli web sitesi

Bu sürüm, mevcut ana sayfa tasarımını değiştirmeden Pages CMS ile makale yayımlama olanağı sağlar.

## İlk kurulum (bir defa)

1. GitHub hesabı oluşturun: https://github.com/
2. **Yeni bir PUBLIC repository** açın (ör. `enesozdemirhukuk`). Site ve makaleler kamuya açık olacağından burada gizli belge veya müvekkil bilgisi bulundurmayın.
3. Bu ZIP içindeki dosyaları, **gizli `.pages.yml` ve `.github` klasörü dahil**, deponun köküne yükleyin. ZIP'i tek dosya olarak yüklemeyin.
4. GitHub deposunda Settings → Pages → Build and deployment → Source kısmında **GitHub Actions** seçin.
5. Actions sekmesinde ilk iş akışını çalıştırın veya `main` dalına değişiklik gönderin. Birkaç dakika sonra GitHub Pages bağlantısı oluşur.
6. https://pagescms.org/ adresinden **GitHub ile giriş** yapın, ilgili depoyu seçin. `Hukuki Makaleler` koleksiyonunda **Yeni** seçeneğiyle makale oluşturun.
7. Başlık, kategori, tarih, özet ve makale metnini girin. Hazır olana kadar **Yayımla** kutusunu kapalı tutun. İşaretleyip kaydettiğinizde GitHub Actions otomatik yeni site sürümünü oluşturur.
8. Siteyi `enesozdemirhukuk.com` alan adına bağlamak için GitHub Settings → Pages → Custom domain alanını kullanın ve alan adı sağlayıcınızda GitHub Pages'in **güncel resmi DNS talimatlarını** uygulayın. Alan adı satın alınmadan bu adım tamamlanamaz.

## Önemli notlar

- Yönetim paneli `pagescms.org` üzerinden açılır; ziyaretçiler paneli görmez. GitHub hesabınızın iki aşamalı doğrulamasını etkinleştirin.
- GitHub Pages ve Pages CMS üçüncü taraf hizmetlerdir; ücretsiz plan koşulları zamanla değişebilir.
- GitHub Pages ücretsiz kullanım için genel (public) depo gerektirebilir. Makaleler yayımlandığında herkese açık olur.
- Bu proje yerel dosyaya çift tıklanarak açılırsa makaleler JSON üzerinden yüklenmeyebilir; yayınlanan site üzerinden test edin.
- Eski ana sayfanın görünümü ve iletişim bilgileri korunmuştur; yayınlanan makaleler 'Yayınlar' bölümünde listelenir.
- Site iletişim formu halen e-posta taslağı açar, sunucuya veri göndermez.
- Gerçek yayından önce KVKK metinlerini, avukatlık reklam mevzuatını ve hukuki içeriklerin doğruluğunu kontrol edin.

## Bilgisayarda önizleme

```bash
pip install -r requirements.txt
python tools/build.py
python -m http.server 8000 --directory dist
```

Ardından http://localhost:8000 adresini açın.
