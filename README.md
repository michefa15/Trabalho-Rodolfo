Trabalho de técnicas de programação

Previsão do mercado de ações usando as técnicas de Deep Learning.
Versão: 1.0, 04 Dezembro/2020
1ª Entrega.

Aluno: Michele Jackeline Andressa Rosa
Professor da disciplina: Rodolfo Stoffel Antunes
Técnicas de programação - PPGCA - Unisinos.
Professor orientador: Sandro Rigo


1. Contexto.

Os investidores sempre tentam tomar as melhores decisões sobre qual melhor ativo que deve ser comprado ou vendido e analisam os movimentos dos mercados financeiros para fazer uma análise precisa de predição para obter os melhores retornos e saber os momentos certo de entrada e saída da Bolsa, e evitar grandes perdas, dado aos riscos e incertezas do mercado financeiro. 
A inteligência artificial vem sendo um campo estudado fortemente nos últimos anos e provando que pode auxiliar nas soluções de problemas complexos, ou seja, as tarefas desempenhadas pelos seres humanos que levam mais tempo para serem desempenhadas, agora são habilitadas para os computadores executar, onde a tarefa que humanos não realizarão as máquinas vêm para auxiliar no processo.
IA vêm provando que tem um potencial para prever os preços do mercado acionário com as técnicas de aprendizado de máquinas e agora vários estudos com algoritmos de aprendizado Deep Learning, devido aos avanços tecnológicos e a grande disponibilidade de recursos computacionais para armazenamento e manipulação de grandes volumes de dados.


2. Descrição da solução.

Implementação do experimento para identificar o comportamento e movimento do mercado acionário, através da aplicação de técnicas de Deep Learning, através do modelo de Long Short Term Memory (LSTM). Assim, possibilitando o desenvolvimento de técnicas mais eficientes para os investidores realizarem alocação dos ativos ao longo do tempo, podendo gerar previsões para melhor desempenho no mercado e nas Bolsas de valores, para melhores tomada de decisões, diante dos riscos e incertezas.


3. Arquitetura do protótipo

O método proposto será validado em experimento usando dados de um ativo listado na Bolsa de Valores brasileira – B3, para averiguar comportamento e movimento das cotações deste ativo, através de técnicas de Deep Learning, através do modelo de Long Short Term Memory (LSTM).  



![alt text](https://raw.githubusercontent.com/michefa15/Trabalho-Rodolfo/main/Figura%2001.png)

Figura 1. Modelo proposto

3.1 Descrição dos Dados

Os dados serão coletados na Plataforma Economatica. A Economatica é uma plataforma de análise de dados de informações financeiras sobre o mercado latino-americano. 
Foram utilizadas 6269 observações diária, das séries temporais de volume das negociações do dia em $ e preço de fechamento que é última cotação no encerramento do mercado, no período de 01 de janeiro de 1995 a 31 de maio de 2020, o início da série foi escolhido ano de 1995 por causa do Plano Real que foi iniciado em 27 de fevereiro de 1994. 
A empresa Petróleo Brasileira S.A. - Petrobras (PETR4.SA), foi ativo escolhido para realização deste experimento, por ser um ativo que compõe o índice Ibovespa e é uma das maiores empresas negociadas na B3, com um valor de mercado de R$ 269.040.164,00 bilhões em maio de 2020 segundo Economatica. 
A pesquisa utilizou de dados de preços e volume $ para previsão do preço de fechamento, com técnica de Deep Learning, através do modelo de Long Short Term Memory (LSTM), procurando aprender e evidenciar padrões e tendências no comportamento do preço do ativo.
Desta forma a implementação do experimento deste estudo do modelo proposto foi realizada por meio da coleta de dados, preparação de dados, escolha do modelo, treinamento, avaliação, aprimoramento dos paramentos e predição, determinar a capacidade do modelo de aprendizagem profunda, para solucionar os problemas.


3.2 Pré-processamento e tratamento dos dados 

No pré-processamento foi realizada a organização e tratamento dos dados para preparação dos dados para os algoritmos da seguinte etapa, sendo responsável para consolidação das informações relevantes para o algoritmo, com intuito de reduzir as dificuldades do problema.
Os dados foram extraídos da plataforma Economatica para uma planilha do Excel, das cotações das séries temporais de quantidades negociadas, quantidade de títulos, volume $, fechamento, abertura, mínimo, máximo e média, do ativo “PETR4” do período de 02/01/1986 a 26/05/2020. Para realização da implementação foram somente utilizados os dados de volume$ e preço de fechamento do período de 01/01/1995 a 26/05/2020.
No pré-processamento foi realizado exclusão dos valores faltantes em branco (sábado, domingo e feriado) que não à funcionamento da Bolsa; preços ajustados por proventos inclusive dividendos; e preço em moeda original. Os valores foram colocados e decimais e data no formato de data.
Antes de alimentar os dados para realização das técnicas de aprendizado profundo, foi realizado um processo de MinMaxScaler para facilitar a convergência no treinamento e generalização na previsão. Para os dados de preço de fechamento e volume $, os atributos de entradas reescalados de forma independente de cada coluna os valores dentro da escala de 0 e 1. Pois os valores absolutos podem variar bastante ao longo prazo, são trocados pela variação de preço pelo tempo, que são padrões mais prováveis de se repetir. Uma proporção de 80 por cento para treinamento e 20 para teste para criação do modelo. 

3.3 Métricas de Desempenho 

Algumas métricas de avaliação foram escolhidas para avaliar quantitativamente o método proposto LSTM, foram utilizadas as métricas: Erro Médio Quadrático – MSE, Raiz Quadrada do Erro Quadrático Médio - RMSE, também foi avaliado pela métricas Erro Médio Absoluto - -MAE e Erro Percentual Absoluto Médio - MAPE.


3.4 Configuração do Ambiente


A linguagem de programação utilizada foi Python 3, onde o desenvolvimento foi realizado na ferramenta do Google Colaboratory (Google Colab) onde permite a criação e execução de códigos em nuvem. Um ambiente virtual foi criado para executar o experimento para este estudo. Neste ambiente virtual, os seguintes pacotes foram instalados: Tensorflow 1.13.1; Keras 2.2.4-tf; Pandas 0.24.2; Sklearn 0.21.1; Numpy 1.16.3 e Matplotlib 3.0.3. Na próxima seção são descritos os resultados do modelo proposto.


4. Resultados e Análise

Esta seção descreve o experimento realizado e resultados obtidos utilizando o modelo descrito na seção anterior. As séries temporais financeiras apresentam alguns comportamentos conhecidos. Os preços dos ativos são não estacionários (raiz unitária), tendo grande volatilidade e muita não linearidade.
Mercado acionário é totalmente incerto, pois os preços das ações têm flutuações diariamente, por conta de inúmeros fatores que influenciam. Desta forma, os investidores buscam sempre ter retorno nos seus investimentos, para isso precisam de ferramentas para analisar o comportamento do preço e a tendência de vários ativos. Neste estudo foi utilizado algoritmo de aprendizado profundo, Long Short Term Memory (LSTM), que tem sido usado para construir modelos de previsão que podem prever os preços das ações e tendência do mercado com boa precisão. Na tabela 1 apresenta as descrições do modelo proposto.


Tabela 1. Descrição do Modelo Proposto

![alt text](https://raw.githubusercontent.com/michefa15/Trabalho-Rodolfo/main/Tabela%201.png)


Os dados foram divididos em: dados de treinamento e dados de teste, resultando 1216 dias para teste, utilizado 5 dias antes para previsão do sexto dia, ou seja, tamanho da janela que se desloca à medida que os dados são lidos, com número de 16 unidades LSTM de neurônios.


![alt text](https://raw.githubusercontent.com/michefa15/Trabalho-Rodolfo/main/Figura%2002.png)

Figura 2. Modelo LSTM

As Medidas de desempenho de previsão de série temporal fornecem informações essenciais sobre a capacidade do modelo de previsão que esperava fazer as previsões. Como mostra a tabela 2 e figura 2 os resultados das métricas utilizadas no modelo proposto.


Tabela 2. Métrica de desempenho

![alt text](https://raw.githubusercontent.com/michefa15/Trabalho-Rodolfo/main/Tabela%202.png)




Para treinamento do modelo foi utilizado 10 por cento da amostra de treinamento para validação do conjunto de dados, sendo epochs de 100 e batch size de 64 é conjunto de entradas que a rede neural irá processar ante de ajustar os pesos do modelo, sendo impactante na velocidade do treinamento, como mostra a tabela 2.
 



![alt text](https://raw.githubusercontent.com/michefa15/Trabalho-Rodolfo/main/Figura%2002.png)

Figura 2. Métrica de desempenho

O MSE apresentou o melhor desempenho como o menor erro, de 0.000176, uma raiz quadrada do erro quadrático Médio de 0.013275, erro médio absoluto de 0.007329, e um erro percentual absoluto médio de 672.771918. 
 




![alt text](https://raw.githubusercontent.com/michefa15/Trabalho-Rodolfo/main/Figura%2004.png)

Figura 3. Séries de preço de fechamento da previsão e preço real

A figura 3 mostra o comportamento das séries de preço das ações PETR4 preço de fechamento real e preço previsto pelo modelo proposto. Os valores dos preços apresentados na figura estão na escala de 0 e 1, mas a mesma pode ser redimensionada para a escala original.
Cada modelo apresenta suas vantagens e desvantagens sobre os fatores de avaliação e os conjuntos de dados usados para os experimentos, alguns modelos funcionam melhor com determinados tipos de dados históricos.

5. Conclusões

A presente pesquisa teve como objetivo estudar as técnicas de inteligência computacional para entendimento e previsão de tendências de preços da Bolsa de valores brasileira, utilizando dados de preço e volume para fazer a previsão por meio de aprendizado profundo, procurando apreender e evidenciar padrões e tendências no comportamento de preços de ativos, onde foi observado o comportamento de um ativo listado na Bolsa de Valores brasileira B3, da empresa Petrobras PETR4 através do modelo de Long Short Term Memory (LSTM). 
Ainda a desafios na previsão do mercado de ações, devido à alta volatilidade e não linearidade dos dados, é uma tarefa desafiadora existentes para previsão de tendências futuras dos preços, tendo a necessidade de novas ferramentas para maior previsibilidade o mercado acionário com exatidão, contudo diversos estudos vêm buscando analisar o comportamento do mercado, através de técnicas Deep Learning e aprimoramentos de modelos como apresentado nos estudos analisados.

