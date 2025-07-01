import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar o dataset
df = pd.read_csv("pokemon.csv")

# 2. Calcular CP estimado
df["cp_estimado"] = np.sqrt(df["base_attack"] * df["base_defense"] * df["base_stamina"])

# 3. Selecionar os 5 Pokémon com maior CP estimado
top5_cp = df.nlargest(5, "cp_estimado")

# 4. Mostrar os dados no terminal com cabeçalhos em português
print("\nTop 5 Pokémon com maior CP estimado:\n")
print(top5_cp[["pokemon_name", "cp_estimado", "base_attack", "base_defense", "base_stamina"]].rename(
    columns={
        "pokemon_name": "Nome do Pokémon",
        "cp_estimado": "CP Estimado",
        "base_attack": "Ataque Base",
        "base_defense": "Defesa Base",
        "base_stamina": "Stamina Base"
    }
))

# 5. Exportar os resultados para CSV e Excel
top5_cp.to_csv("top5_pokemon_cp.csv", index=False)
top5_cp.to_excel("top5_pokemon_cp.xlsx", index=False)

# 6. Gráfico de barras comparando atributos
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Atributos a comparar (mantém nomes originais para facilitar visualização)
atributos = ["base_attack", "base_defense", "base_stamina", "cp_estimado"]
top5_melted = top5_cp.melt(
    id_vars="pokemon_name",
    value_vars=atributos,
    var_name="Atributo",
    value_name="Valor"
)

# Traduzindo valores de "Atributo" para o gráfico
mapa_atributos = {
    "base_attack": "Ataque Base",
    "base_defense": "Defesa Base",
    "base_stamina": "Stamina Base",
    "cp_estimado": "CP Estimado"
}
top5_melted["Atributo"] = top5_melted["Atributo"].map(mapa_atributos)

# Plot
sns.barplot(data=top5_melted, x="pokemon_name", y="Valor", hue="Atributo", palette="Set2")
plt.title("Top 5 Pokémon por CP Estimado — Comparação de Atributos")
plt.xlabel("Pokémon")
plt.ylabel("Valor")
plt.legend(title="Atributo")
plt.tight_layout()
plt.savefig("grafico_top5_pokemon_cp.png")  # Salvar imagem
plt.show()

print("\n✅ Gráfico salvo como 'grafico_top5_pokemon_cp.png'")
