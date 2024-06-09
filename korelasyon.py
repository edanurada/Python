import pandas as pd
import numpy as np

# İlk veri setini oku
first_data = pd.read_excel("tablo.xlsx")

# İkinci veri setini oku
second_data = pd.read_excel("tablo2.xlsx")

# Yalnızca sayısal sütunları seç
first_numeric_columns = first_data.select_dtypes(include=[np.number]).columns
first_data = first_data[first_numeric_columns]

second_numeric_columns = second_data.select_dtypes(include=[np.number]).columns
second_data = second_data[second_numeric_columns]

# İlk veri setinin özelliklerinin korelasyonunu hesapla
first_correlation = first_data.corr()

# İkinci veri setinin özelliklerinin korelasyonunu hesapla
second_correlation = second_data.corr()

# İki korelasyon matrisi arasındaki Pearson korelasyon katsayısını hesapla
common_features = list(set(first_correlation.columns).intersection(second_correlation.columns))
first_correlation_common = first_correlation.loc[common_features, common_features]
second_correlation_common = second_correlation.loc[common_features, common_features]

# Pearson korelasyon katsayısını hesapla
pearson_correlation = np.corrcoef(first_correlation_common.values.flatten(), second_correlation_common.values.flatten())[0,1]

# Korelasyon matrislerini yazdır
print("İlk Veri Seti Korelasyon Matrisi:")
print(first_correlation)

print("\nİkinci Veri Seti Korelasyon Matrisi:")
print(second_correlation)

# Benzerlik oranını yazdır
print("İki veri seti arasındaki Pearson Korelasyon Katsayısı:", pearson_correlation)
