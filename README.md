# Smart City Traffic and Air Quality Analysis

Bu proje, Kaggle'dan alınan iki büyük gerçek veri setini (Trafik Hacmi ve Hava Kalitesi) kullanarak temel veri bilimi, "feature engineering", veri birleştirme (merge) ve korelasyon analizlerini Pandas ve NumPy kütüphaneleriyle gösteren örnek bir uygulamadır.

## 📌 Proje Adımları

1. **Veri Yükleme:** Pandas `read_csv` ile trafik ve hava durumu veri setlerinin projeye dahil edilmesi.
2. **Veri Temizleme:** 
   - İçi boş tatil (`is_holiday`) günlerinin tespiti ve veri kaybı olmadan temizlenmesi (`fillna`).
   - `.csv` içerisindeki gizli ve hatalı Unnamed sütunlarının tespit edilip silinmesi.
3. **Feature Engineering:** `np.where` metodu kullanılarak trafik hacminin yoğunluk kategorilerine (Yüksek/Orta/Düşük) ayrılması.
4. **Zaman Bazlı Özellikler:** `date_time` yapılarına dönüştürme ve iki veri setinin eşzamanlı birleşimi (merge) için veri bilimi tarih kaydırma yöntemlerinin uygulanması.
5. **Veri Birleştirme:** `pd.merge` ile verilerin tarih/saat odağında birleştirilmesi.
6. **Gruplandırma (Groupby):** Saatlere göre azot diyoksit oranındaki (NO2) artışların bulunması.
7. **Korelasyon:** Veri setindeki sıcaklık, saat, trafik hacmi ve rüzgar hızı gibi nümerik korelasyonların matrisinin çıkartılması.
8. **Pivot Table ve Indexleme:** Değişkenler arası ilişkilerin matris formatında raporlanması.

### Gereksinimler
- Python 3.10+ sürümü 
- `pandas`
- `numpy`

### Veri Setleri
Eğer repo içerisinde yüklü değilse, projeyi çalıştırmak için aşağıdaki verileri Kaggle üzerinden indirip ana dizine atmanız gerekir:
1. `TrafficVolumeData.csv`
2. `AirQualityUCI.csv`

## 📋 Örnek Çıktılar
- `Trafik Eksik Veriler` ve temizlenme süreç raporu.
- Saat ve trafik yoğunluk düzeylerine göre saatlik hava kirlilik ortalamaları.
- Hava Kalitesi ve Trafik verilerini kıyaslayan numerik korelasyon matrisi.
