# Projeto de Estatística Aplicada

## 🧑‍💻 Autores  
- Renato Miguel (202421250029) - renato.miguel@academico.ifpb.edu.br  
- José Kauê (202421250035) - alves.kaue@academico.ifpb.edu.br  
- Bruno de Paula (202421250031) - paula.bruno@academico.ifpb.edu.br  

## 🎯 Tema e Motivação  
Este projeto tem como objetivo mostrar características sobre os pokemons dentro do jogo Pokemon GO, características essas como tipos, atributos, status, raridades, conjunto de movimentos, status de batalha e estatísticas básicas. O tema foi escolhido com intuito de informar estatísticamente e de forma enxuta o sistema de jogo do Pokemon GO.

Ele será de grande ajuda para quem quer aprofundar os conhecimentos em Pokemon GO, assim melhorando a jogabilidade do jogador, conhecimentos de batalha, tipos, raridades e etc.

## 📊 Conjunto de Dados Selecionado  
- **Nome do conjunto de dados:**  
  Gotta Analyze 'Em All: The Ultimate Pokémon GO Dataset

- **Fonte:**  
  https://www.kaggle.com/datasets/shreyasur965/pokemon-go/data

- **Descrição breve:**  
  O conjunto representa uma variedade de dados de um único pokemon, cria ferramentas para os jogadores otimizarem suas estratégias de jogo, apresenta fraquezas e vantagens de cada pokemon.   

- **Justificativa para a escolha:**  
  Pois ele consegue selecionar várias variáveis de um pokemon e comparar com outros de forma simples, tornando mais fácil a compreensão e funcionalidade do sistema de jogo.

---

## ❓ Perguntas ou Hipóteses  
*Começar a planejar com perguntas de Estatística Descritiva*  
- Existe algum status básico que seja mais presente que outros?.
- Qual o tipo de pokémon mais utilizado comparado aos outros?
- Qual a correlação dos itens do jogo, com a captura de pokemons com raridades diferentes?

## 🔍 Metodologia  
#### Foi usado técnicas de correlação, dsitribuição e comparação. Sempre mantendo um padrão de tabelas em markdown para ser mais légivel, apresentável e melhor compreendido. 
#### Também utilizado uma biblioteca, o matplotlib, para os visuais de gráficos estatísticos e melhor visão de dispariedade de variáveis, distribuição e comparação.

## 🛠️ Ferramentas Utilizadas 

#### - IDE utilizada -> VSCode.
#### - Bibliotecas - Numpy, Pandas, Matplotlib e Seaborn.
#### - Dataset - Excel.
#### - Linguagem utilizada - Python.

## 📈 Resultados  
### Resultados obtidos a partir dos códigos em pyhton.

#### Tabela de comparação de CP entre pokemons lendários e não lendários.


|Pokemons | Contagem | Média | Mediana | Mínimo | Máximo | Desvio Padrão |
| --------- | -------- | ----- | ----------- | ---------- | ------------| ---------------- |
|Lendário   | 64  |   4024    | 4028  | 494 | 9366 | 1086  |
|Não Lendário| 943 | 2193   |  2170   | 16 | 5418 | 1022  | 


<img width="1200" height="600" alt="gráfico de colunas pokemon" src="https://github.com/user-attachments/assets/824661dd-3d17-4b16-9692-cd3cc5c0caf1" />


#### Taxas de fuga entre pokemons com HP alto e baixo.


Pokemons| Contagem | Média | Máximo | Mínimo | Desvio-Padrão|
|----|----|----|----|-----|------|
HP Alto| 213 | 237 | 496 | 202 | 46 |
HP Baixo| 794 | 153 | 200 | 0 | 28 |


#### 5 Pokemons com o maior CP e suas características.


Nome do Pokemon| CP | Ataque Base | Defesa Base | Stamina Base |
|----|----|----|----|-----|
Eternatus | 7569 | 251 | 505 | 452 |
Zacian | 3911 | 332 | 240 | 192 |
Zygard | 3849 | 184 | 207 | 389 |
Palafin | 3768 | 322 | 196 | 225 |
Lugia | 3749 | 193 | 310 | 235 |


<img width="1200" height="600" alt="grafico_top5_pokemon_cp" src="https://github.com/user-attachments/assets/41c91786-ffb8-4701-8a44-28f0d2e66a45" />


## 📌 Conclusões  

#### O aprendizado sintetizado, em sua maior parte, foi a implementação dos códigos e análise do dataset, pois houve o primeiro contado com o dataset e os códigos em python para resolução de problemas estatísticos, comparações ou testes hipotéticos.

#### As análises podem ser revisadas e até refeitas através de issues, e até mesmo utilizadas para fins de pesquisas.

## ⚠️ Limitações e Trabalhos Futuros  

#### Houve a falta de dados em certas análises pois o dataset estava incompleto, pois sempre há novos pokemons e é adicionado cada característica por pokemon.

#### Também a falta de experiência com os códigos e bibliotecas. Ainda falta bastante conhecimento nas bibliotecas para ter uma boa análise de dados. 

---

