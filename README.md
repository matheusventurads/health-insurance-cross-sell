# Insurance Cross Sell Prediciton
# Conhecendo o negócio
 A Soter Insurance, é uma seguradora indiana fictícia, empresa que atua no mercado financeiro com foco na emição de apólices de seguros de saúde. Uma apólice de seguro é um acordo pelo qual uma empresa se compromete a fornecer uma garantia de compensação por perda, dano, doença ou morte especificados em troca do pagamento de um prêmio especificado. Um prêmio é uma quantia em dinheiro que o cliente precisa pagar regularmente a uma companhia de seguros por essa garantia.

# 1. Questão de negócio
A empresa planeja realizar 20 mil divulgações do novo seguro aos atuais clientes, e com o intuito de priorizar os interessados e maximizar os lucros é necessário prever se os clientes que contrataram um seguro de saúde do último ano também estão interessados em seguros de veículos fornecidos pela empresa. 

## 1.1. Entendendo os dados
Para realizar a predição estão disponíveis dados demográficos, dos veículos e apólices de clientes com suas repostas.
|Atributo|Definição|
|--------|---------|
|id| ID único para cada cliente|
|Gender|Gênero do cliente|
|Age| Idade do cliente|
|Driving_License|0: Clinte não tem CNH, 1: Cliente já tem CNH|
|Region_Code|Código único para a região do cliente|
|Previously_Insured|0: Cliente não tem seguro de veículo, 1: Cliente já tem um seguro de veículo|
|Vehicle_Age| Idade do veículo|
|Annual_Premium| O valor do prêmio que o cliente pagará no ano|
|Policy_Sales_Channel|Código anonimizado do canal de divulgação ao cliente, ex: diferentes representantes, pelo correio, pelo telefone, em pessoa, etc.|
|Vintage|Número de dias que o cliente é associado à empresa|
|Response|0: Cliente não está interessado, 1: Cliente está interessado

# 2. Premissas de negócio
* O objetivo é elencar os clientes com maior propensão de contratar o seguro.
* Serão realizados 20 mil contatos com os clientes para oferta do seguro.

# 3. Planejamento da solução
O planejamento foi dividido em três etapas:

## 3.1. Produto Final
O resultado entregue será uma planilha no Google Sheets que apresenta a propensão de cada cliente de interesse no seguro, ranqueando-os em relação a propensão.

## 3.2. Processo
### _Entendendo o problema de negócio_
Entender a motivação para a previsão e assim planejar a solução mais efetiva.

### _Coleta de dados_
Coleta dos dados dos clientes e respostas na plataforma [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).

### _Limpeza dos dados_
Colunas renomeadas.

### _Análise Exploratória de Dados (EDA)_
Exploração dos dados para entendimento de negócio e descoberta de insights para auxílio na determinação de features no treinamento do modelo de machine learning.

### _Feature Enginnering_
Transformação de features para facilitar a análise e preparação para os modelos de machine learning.

### _Preparação dos dados
Aplicação de técnicas de normalização, rescaling e encoding dos dados.

### _Feature Selection_
Seleção das features relevantes que serão utilizadas para treinamento do modelo através do algoritmo ExtraTree.

### _Machine Learning Modeling_
Treinamento de algoritmos de Classificação com cross-validation estratificada. O modelo selecionado foi aperfeiçoado com Hyperparameter fine tuning.

### _Avaliação do Modelo_
Avaliação do modelo treinado utilizando das seguintes técnicas: _Precision at k_ e _Recall at k_.

### _Resultados Financeiros_
Tradução do resultado para valores de negócio.

### _Deploy do Modelo (Google Sheets)_
Implementação da API para previsão da propensão de cada cliente em planilha online do Google Sheets.

## 3.3. Ferramentas

* Python 3.8
* Pandas, Seaborn, Matplotlib e Sklearn
* Flask e Python API's
* Git e Heroku
* Boruta
* Algoritmos de Classificação (k-Nearest Neighbors, Regressão Logística, Random Forest, XGBoost, LightGBM e CatBoost)
* Cross-Validation, Hyperparameter Optimization
* Métricas de Performance (Precision at k, Recall at k)

# 4. Destaque dos Insights de negócio
Na exploração de dados, foram levantadas diferentes hipóteses para melhor entendimento do comportamento de cada atributo. Dentre as hipóteses, os seguintes insights foram destacados.

# 5. Modelos de Machine Learning
Foram treinados 6 modelos de machine learning para previsão das vendas, com cross-validation:
* Modelo Aleatório (Baseline para análise de performance)
* KNN (k nearest neighbors)
* Regressão Logística
* Random Forest Classifier
* XGBoost Classifier
* LightGBM Classifier
* CatBoost Classifier

Abaixo estão as performances de cada modelo em ordem crescente:

|Modelo|Precision at k|Recall at k|
|------|--------------|-----------|
|LightGBM Classifier|0,3026 +/ -0,0021|0,863 +/- 0,0059|
|CatBoost Classifier|0,3014 +/- 0,0022|0,8605 +/- 0,0063|
|XGBoost Classifier	|0,3012 +/- 0,0022|0,8597 +/- 0,0064|
|Random Forest Classifier|0,286 9+/- 0,0026|0,8189 +/- 0,0074|
|KNeighbors Classifier|0,2794 +/- 0,0019|0,7975 +/- 0,0056|
|LogisticRegression|0.275 +/- 0,002|0,785 +/- 0,0057|

O modelo escolhido foi LightGBM, que além de apresentar os melhores valores para as métricas analisadas, também tem alta velocidade de treinamento, facilitando o estudo dos hiperparâmetros para otimização.

Após otimização pelo método de Random Search, o modelo foi treinado com os novos valores de hiperparâmetros e os seguintes resultados foram obtidos na previsão de propensão nos dados de teste.

|Modelo|Precision at k|Recall at k|
|------|--------------|-----------|
|LightGBM Classifier|0,3536|0,6056|

## Entendendo as métricas
* Precision at k: dentre _k_ classificações de classe Positivo que o modelo fez, quantas estão corretas, ou seja, quantas realmente eram positivas.
* Recall at k: porcentagem de classificações de classe Positivo em _k_ previsões que o modelo fez, em relação ao total de classificações positivas.

### Gráficos
* Cumulative Gain Curve: curva que indica a porcentagem da classe positiva em relação a porcentagem dos dados, com base na propensão prevista.
* Curva Lift: indica quantas vezes o modelo de machine learning treinado é melhor do que o modelo aleatório.

Como restrição de negócio, k é igual a 20.000. A primeira vista, o valor de _Precision at k_ aparenta ser baixo, pois do total de predições feitas apenas _35,36%_ realmente são positivas. Porém o objetivo é elencar os clientes com maior propensão, que pode ser melhor analisado pela _Recall at k_, que aponta que com 20 mil contatos realizados, _60,56%_ de todos os clientes com resposta positivas foram alcançados.

# 6. Resultado de negócio
Para determinar os resultados financeiros, as seguintes premissas foram definidas:
* O número de clientes na base de dados será 95.278, onde 11678 clientes estão interessados no seguro.
* Com base nos dados de treino, é esperado que 12,26% dos clientes estejam interessados (Modelo Aleatório).
* O valor do prêmio anul é de ₹31.669 (rúpias), mediana dos valores na base de dados.

|Modelo|Clientes interessados alcançados|Receita Anual|
|------|--------------------------------|-------------|
|LightBGM|7.071|₹223,932,417.40|
|Modelo Aleatório|2.451|₹77,627,439.16|
|Diferença|4.620|₹146.304.978,24|

Assim, o resultado financeiro esperado com o modelo de Machine Learning é 288% maior do que o que seria alcançado com o modelo aleatório. Como visto na Curva Lift.

# 7. Deploy do modelo
# 8. Conclusão
# 9. Próximos passos
