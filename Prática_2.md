## **📚 Projeto de Estatística Aplicada – Prática 02**

Nesta prática, você vai **conhecer e entender a estrutura do conjunto de dados**, antes de iniciar qualquer análise estatística.

O objetivo é se **familiarizar** com o dataset que você escolheu, observando:

- Essas são as informações principais do dataset, pois ele cobre uma variedade de informções mais complexas.

    #### -Cobertura completa de 1007 Pokémon.
    #### -24 atributos para cada Pokémon, incluindo estatísticas de batalha, tipo e raridade
    #### -Informações sobre métodos de aquisição (selvagem, ovo, ataque, etc.)
    #### -Detalhes do conjunto de movimentos para movimentos rápidos e carregados
    #### -Dados da mecânica do jogo, como taxas de captura e fuga.

- As informações estão organizadas em tabelas, gráficos de dispersão, mapa de calor de correlação de características numéricas.

- Quantitativas e Qualitativas.

---

## 🛠️ O que você deve fazer:

1. https://www.kaggle.com/code/shreyasur965/pokemon?scriptVersionId=191238467&cellId=1.
2. https://www.kaggle.com/code/shreyasur965/pokemon?scriptVersionId=191238467&cellId=2.

6. **Carregar o seu dataset** para dentro do ambiente de trabalho.

    - https://www.kaggle.com/code/shreyasur965/pokemon?scriptVersionId=191238467&cellId=3.

7. **Visualizar as primeiras linhas** do dataset para entender como as informações estão organizadas.
   
    - https://www.kaggle.com/code/shreyasur965/pokemon?scriptVersionId=191238467&cellId=5

9. **Descobrir o tamanho** do dataset:

    - https://www.kaggle.com/code/shreyasur965/pokemon?scriptVersionId=191238467&cellId=4.

    - https://www.kaggle.com/code/shreyasur965/pokemon?scriptVersionId=191238467&cellId=6.

10. **Listar todas as variáveis** disponíveis no dataset.
    
    - https://www.kaggle.com/code/shreyasur965/pokemon?scriptVersionId=191238467&cellId=4

12. **Identificar o tipo de dado** de cada variável:

    - **Quantitativas**: Está contabilizado na tabela do ponto 13.

    - **Qualitativas**: Está contabilizado na tabela do ponto 13.

13. **Organizar** essa classificação em uma pequena tabela para visualização.

| Variável             | Tipo de dado (pandas) | Classificação Estatística | Descrição breve                      |
| -------------------- | --------------------- | ------------------------- | ------------------------------------ |
| `#`                  | int64                 | Quantitativa              | Número na Pokédex                    |
| `Name`               | object                | Qualitativa               | Nome do Pokémon                      |
| `Type 1`             | object                | Qualitativa               | Tipo primário (ex: Água, Fogo)       |
| `Type 2`             | object                | Qualitativa               | Tipo secundário (pode ser vazio)     |
| `Total`              | int64                 | Quantitativa              | Soma dos stats base                  |
| `HP`                 | int64                 | Quantitativa              | Vida base                            |
| `Attack`             | int64                 | Quantitativa              | Ataque base                          |
| `Defense`            | int64                 | Quantitativa              | Defesa base                          |
| `Sp. Atk`            | int64                 | Quantitativa              | Ataque especial base                 |
| `Sp. Def`            | int64                 | Quantitativa              | Defesa especial base                 |
| `Speed`              | int64                 | Quantitativa              | Velocidade base                      |
| `Generation`         | int64                 | Quantitativa (discreta)   | Geração do Pokémon (1 a 8)           |
| `Legendary`          | bool / object         | Qualitativa (dicotômica)  | Se é lendário (True/False)           |
| `Capture Rate`       | float64 / object      | Quantitativa              | Taxa base de captura                 |
| `Flee Rate`          | float64 / object      | Quantitativa              | Taxa base de fuga                    |
| `Fast Moves`         | object                | Qualitativa (lista)       | Ataques rápidos disponíveis          |
| `Charged Moves`      | object                | Qualitativa (lista)       | Ataques carregados disponíveis       |
| `Is Shiny Available` | bool / object         | Qualitativa (dicotômica)  | Se possui forma shiny disponível     |
| `Is Egg Available`   | bool / object         | Qualitativa               | Se pode nascer de ovo                |
| `Egg Distance (km)`  | float64 / object      | Quantitativa              | Distância para chocar (em km)        |
| `Is Raid Boss`       | bool / object         | Qualitativa               | Se aparece em raids                  |
| `Region`             | object                | Qualitativa               | Região de origem (Kanto, Johto etc.) |
| `Form`               | object                | Qualitativa               | Forma especial (ex: Alolan)          |

## 🧠 Competências Trabalhadas

- Leitura e interpretação inicial de datasets.

- Compreensão de tipos de variáveis.

- Organização sistemática de informações.

- Preparação para análise exploratória de dados (EDA).

---

## 📝 Entrega Esperada

Ao final da prática, você deverá apresentar:

- O código organizado, rodado passo a passo.

- As seguintes informações sobre o seu dataset:

    - Número total de registros (linhas) e variáveis (colunas).

    - Lista das variáveis classificadas como quantitativas.

    - Lista das variáveis classificadas como qualitativas.

    - Uma tabela resumo separando as variáveis por tipo.

**Obs.:** Cada aluno deverá utilizar o **dataset que escolheu** para o seu projeto.
​
⚠️ ​Se você decidir usar outra ferramenta (Excel, Power BI, Tableau, etc), crie um arquivo de texto com as mesmas informações acima. 


### **O arquivo gerado devem ser colocados no github do seu projeto até quarta-feira, 07/05.**

---

## 💬 Dicas

- Não tenha pressa: explore o seu dataset com calma.

- Se alguma variável for difícil de classificar, anote sua dúvida para discutirmos em aula.

- Aproveite este momento para se familiarizar bem com os dados — isso vai facilitar muito nas próximas etapas do projeto.

---

