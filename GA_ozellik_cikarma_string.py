import pandas as pd
from deap import base, creator, tools, algorithms
import numpy as np

# Verileri okuma
df1 = pd.read_excel("1.veri_yolu.xlsx")
df2 = pd.read_excel("2.veri_yolu.xlsx")
df3 = pd.read_excel("3.veri_yolu.xlsx")
df4 = pd.read_excel("4.veri_yolu.xlsx")

# Her bir veri setine etiket ekle 
df1['etiket'] = 0
df2['etiket'] = 1
df3['etiket'] = 2
df4['etiket'] = 3

# Veri setlerini birleştir
merged_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

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

# Hedef fonksiyonunu tanımla (Burada özelleştirme yapmanız gerekebilir)
def evaluate(individual):
    selected_features = [feature for feature, sel in zip(features, individual) if sel]
    # Burada, seçilen özelliklere dayalı bir performans ölçütü hesaplamalısınız
    # Örneğin, seçilen özelliklere dayalı bir model eğitebilir ve doğruluk oranını ölçebilirsiniz.
    # Bu kısmı ihtiyaçlarınıza göre özelleştirmeniz gerekecek
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

# Filtrelenmiş veriyi oluştur
filtered_data = merged_df[selected_features + ['etiket']]

# Seçilen özelliklere sahip yeni bir tablo oluştur
new_table = merged_df[selected_features + ['etiket']].copy()

# Yeni tabloyu yazdır veya kaydet
print(new_table)
new_table.to_excel("tablo.xlsx", index=False)
