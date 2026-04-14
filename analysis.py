import pandas as pd
import numpy as np

# 1. Veri Yükleme
print("Veriler yükleniyor...")
traffic = pd.read_csv("TrafficVolumeData.csv")
air = pd.read_csv("AirQualityUCI.csv")

# 2. Veri Temizleme
print("\n--- Eksik Veri Kontrolü ---")
print("Trafik Eksik Veriler:\n", traffic.isnull().sum())
print("\nHava Kalitesi Eksik Veriler:\n", air.isnull().sum())

traffic.fillna({"is_holiday": "Tatil Degil"}, inplace=True)
traffic.dropna(inplace=True)

# Hava Kalitesi (air) verisinde ise en sonda tamamen boş gizli sütunlar vardı.
# Önce tamamen boş "sütunları" siliyoruz, sonra boş "satırları" siliyoruz.
air.dropna(axis=1, how='all', inplace=True)
air.dropna(inplace=True)

# 3. Numpy ile Feature Engineering
traffic["yogunluk_seviyesi"] = np.where(
    traffic["traffic_volume"] > 5000, "Yüksek",
    np.where(traffic["traffic_volume"] > 2500, "Orta", "Düşük")
)

# 4. Zaman Bazlı Özellikler (Sütunlar Türkçeleştirildi)
traffic["tarih_saat"] = pd.to_datetime(traffic["date_time"])
traffic["saat"] = traffic["tarih_saat"].dt.hour

# Air (Hava Kalitesi) verisinde "Date" ve "Time" alanlarını birleştirip tarih_saat oluşturuyoruz
air["tarih_saat"] = pd.to_datetime(air["Date"] + " " + air["Time"], errors='coerce')


# Hava kalitesi verisi 2004'te, trafik verisi 2012 Ekim ayında başlıyor.
air["tarih_saat"] = air["tarih_saat"] + pd.Timedelta(days=3128)

# 5. Veri Birleştirme (Merge)
df = pd.merge(traffic, air, on="tarih_saat")

df.rename(columns={"traffic_volume": "trafik_hacmi", "NO2(GT)": "azot_diyoksit_kirliligi"}, inplace=True)

# 6. Gruplandırma Analizi
print("\n--- 6. Gruplandırma Analizi (Saatlik Ortalama Kirlilik) ---")
saatlik_kirlilik = df.groupby("saat")["azot_diyoksit_kirliligi"].mean()
print(saatlik_kirlilik)

# 7. Korelasyon Analizi
print("\n--- 7. Korelasyon Analizi ---")
korelasyon = df.select_dtypes(include=[np.number]).corr()
print(korelasyon)

# 8. Multi Index Kullanımı
print("\n--- 8. Multi Index Analizi (Saat ve Yoğunluğa Göre Kirlilik) ---")
multi_analiz = df.groupby(["saat", "yogunluk_seviyesi"])["azot_diyoksit_kirliligi"].mean()
print(multi_analiz)

# 9. Pivot Table
print("\n--- 9. Pivot Table ---")
pivot_tablo = pd.pivot_table(df, values="azot_diyoksit_kirliligi", index="saat", columns="yogunluk_seviyesi")
print(pivot_tablo)

# 10. Ek Analiz
df["yuksek_kirlilik_mi"] = np.where(df["azot_diyoksit_kirliligi"] > 100, 1, 0)

print("\n--- 10. Ek Analiz Sonuç (İlk 5 Satır) ---")
print(df[["tarih_saat", "trafik_hacmi", "yogunluk_seviyesi", "azot_diyoksit_kirliligi", "yuksek_kirlilik_mi"]].head())
