import pandas as pd
import numpy as np
from deap import base, creator, tools, algorithms

# Hexadecimal stringi integer'a dönüştürme fonksiyonu
def hex_to_int(value):
    # Eğer değer bir sayısal değerse, doğrudan değeri döndür
    if isinstance(value, (int, float)):
        return value
    try:
        # Değeri onaltılık bir tamsayıya dönüştür
        return int(value, 16)
    except ValueError:
        # Eğer dönüştürme başarısız olursa, değeri olduğu gibi döndür
        return value


# Verileri okuma
df1 = pd.read_excel("1.veri_yolu.xlsx")
df2 = pd.read_excel("2.veri_yolu.xlsx")
df3 = pd.read_excel("3.veri_yolu.xlsx")
df4 = pd.read_excel("4.veri_yolu.xlsx")

# Her bir veri setine etiket ekle (36. sütuna)
df1['etiket'] = 0
df2['etiket'] = 1
df3['etiket'] = 2
df4['etiket'] = 3

# Veri setlerini birleştir
merged_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Eksik değerleri sil
merged_df.fillna(0, inplace=True)  # Boş değerleri 0 ile doldur

# Hexadecimal stringi integer'a dönüştür
string_columns = merged_df.select_dtypes(include=[object]).columns
for column in string_columns:
    merged_df[column] = merged_df[column].apply(hex_to_int)

# Genetik algoritma için uygun formatta veriyi hazırla
features = merged_df.columns[:-1]  # Etiket sütununu dahil etme
data = merged_df[features].values
labels = merged_df['etiket'].values

# Genetik Algoritma Parametreleri
POPULATION_SIZE = 50
CROSSOVER_PROBABILITY = 0.7
MUTATION_PROBABILITY = 0.2
GENERATIONS = 10

# Genetik algoritma için uygun fonksiyonları tanımla
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", np.random.choice, [0, 1], size=len(features))
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr_bool)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Hedef fonksiyonunu tanımla
def evaluate(individual):
    selected_features = [feature for feature, sel in zip(features, individual) if sel]
    # Burada, seçilen özelliklere dayalı bir performans ölçütü hesaplamalısınız
    # Örneğin, seçilen özelliklere dayalı bir model eğitebilir ve doğruluk oranını ölçebilirsiniz.
    # Bu kısmı ihtiyaca göre özelleştirmelisiniz
    return (np.random.rand(),)  # Rastgele değer döndürüldü, gerçek bir performans ölçütü ekleyin

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Popülasyonu oluştur
population = toolbox.population(n=POPULATION_SIZE)

# Genetik algoritmayı çalıştır
algorithms.eaMuPlusLambda(population, toolbox, mu=POPULATION_SIZE, lambda_=2*POPULATION_SIZE,
                          cxpb=CROSSOVER_PROBABILITY, mutpb=MUTATION_PROBABILITY,
                          ngen=GENERATIONS, stats=None, halloffame=None, verbose=True)

# En iyi bireyi seç
best_individual = tools.selBest(population, k=1)[0]
selected_features = [feature for feature, sel in zip(features, best_individual) if sel]

# Seçilen özelliklere sahip yeni bir tablo oluştur
new_table = merged_df[selected_features + ['etiket']].copy()

# Yeni tabloyu yazdır veya kaydet
print(new_table)
new_table.to_excel("tablo2.xlsx", index=False)
