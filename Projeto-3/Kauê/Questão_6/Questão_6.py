import pandas as pd
import numpy as np

# Carregar os dados
df = pd.read_csv('pokemon.csv')  # Substitua pelo seu arquivo real

# 1. Calcular a mediana do HP
hp_median = df['base_stamina'].median()

# 2. Criar grupos
df['hp_group'] = np.where(df['base_stamina'] > hp_median, 'Acima da Mediana', 'Abaixo da Mediana')

# 3. Análise descritiva por grupo
flee_stats = df.groupby('hp_group')['dodge_probability'].agg(['mean', 'median', 'std', 'min', 'max'])
