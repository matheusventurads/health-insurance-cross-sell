# Insurance Cross Sell Prediciton
# Conhecendo o negócio
 A Soter Seguros, é uma seguradora fictícia, empresa que atua no mercado financeiro com foco na emição de apólices de seguros de saúde. Uma apólice de seguro é um acordo pelo qual uma empresa se compromete a fornecer uma garantia de compensação por perda, dano, doença ou morte especificados em troca do pagamento de um prêmio especificado. Um prêmio é uma quantia em dinheiro que o cliente precisa pagar regularmente a uma companhia de seguros por essa garantia.

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
# 5. Modelos de Machine Learning
# 6. Resultado de negócio
# 7. Deploy do modelo
# 8. Conclusão
# 9. Próximos passos
