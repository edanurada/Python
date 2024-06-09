import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, f1_score

# Yeni oluşturulan tabloyu oku
new_table = pd.read_excel("tablo.xlsx")

# Sadece sayısal değerlere sahip sütunları seç
numeric_columns = new_table.select_dtypes(include=[np.number]).columns
new_table = new_table[numeric_columns]

# Boş değerleri doldur
new_table.fillna(0, inplace=True)  # Boş değerleri 0 ile doldur

# Verileri ve etiketleri tekrar ayır
features = new_table.columns[:-1]
data = new_table[features].values
labels = new_table['etiket'].values

# Veri kümesini eğitim ve test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Modeli eğit
rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

# Modelin performansını değerlendir
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Performans ölçütlerini yazdır
print("Accuracy:", accuracy)
print("Precision:", precision)
print("F1 Score:", f1)
