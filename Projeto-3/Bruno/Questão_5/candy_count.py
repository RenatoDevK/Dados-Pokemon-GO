import pandas as pd
import matplotlib.pyplot as plt
import ast

# Carrega o dataset
df = pd.read_csv('pokemon.csv')

# Remove valores nulos e copia os dados
df_limpo = df.dropna(subset=['candy_required']).copy()

# Corrige a coluna 'type' para extrair apenas o primeiro tipo, removendo colchetes
df_limpo.loc[:, 'type'] = df_limpo['type'].apply(
    lambda x: ast.literal_eval(x)[0] if isinstance(x, str) and x.startswith('[') else x
)

# Tradução dos tipos (opcional)
traducao_tipos = {
    'Dragon': 'Dragão',
    'Fairy': 'Fada',
    'Ghost': 'Fantasma',
    'Flying': 'Voador',
    'Steel': 'Metálico',
    'Fighting': 'Lutador',
    'Fire': 'Fogo',
    'Water': 'Água',
    'Grass': 'Grama',
    # Adicione mais se quiser
}

# Agrupa por tipo e calcula média e desvio padrão
estatisticas = df_limpo.groupby('type')['candy_required'].agg(['mean', 'std'])

# Seleciona os 3 tipos com maior média
top3 = estatisticas.sort_values(by='mean', ascending=False).head(3)

# Traduz nomes (se possível)
top3.index = top3.index.map(lambda t: traducao_tipos.get(t, t))

# Exibe os dados no terminal
top3 = top3.rename_axis("Tipo")
print("Top 3 Tipos Primários que mais exigem doces para evoluir:")
print(top3.rename(columns={'mean': 'Média de Doces', 'std': 'Desvio Padrão'}))

# Gera o gráfico
plt.figure(figsize=(8, 5))
plt.bar(top3.index, top3['mean'], yerr=top3['std'], capsize=10, color='royalblue')
plt.title('Top 3 Tipos Primários que Mais Exigem Doces para Evoluir')
plt.xlabel('Tipo Primário')
plt.ylabel('Quantidade Média de Doces')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Salva e mostra o gráfico
plt.savefig('grafico_top3_tipos_doces.png')
plt.show()
