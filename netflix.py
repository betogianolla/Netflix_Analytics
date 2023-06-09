import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('NetflixDataset.csv')

data.info()

#Removendo dados duplicados.
data.drop_duplicates(inplace = True)
data[data.duplicated()]
#Encontrando dados nulos e expondo em um heatmap.
data.isnull().sum()
sns.heatmap(data.isnull())

"""### Q1) Para "House of Cards", qual é o Show Id e quem é o Diretor?

"""

data[data['Title'].isin(['House of Cards'])]

"""R1: ID: s2833 - Diretor: Robin Wright, David Fincher, Gerald McRaney, J...

#Q2) Em que ano houve o maior número de lançamentos de séries e filmes foram lançados? Mostre com um gráfico de barras.
"""

#Criando uma nova coluna, contendo o formato tempo
data['Date_N'] = pd.to_datetime(data['Release_Date'])

#Contando as ocorrências de todos os anos individuais na coluna Date_N
data['Date_N'].dt.year.value_counts()

#Criando o gráfico
data['Date_N'].dt.year.value_counts().plot(kind='bar')

"""R2) O ano com maior número de lançamentos (séries e filmes) é 2019, com 2153 lançamentos, seguido por 2020 com 2009 lançamentos.

##Q3) Quantos filmes e séries tem nesse dataset? Mostre em um gráfico de barras.
"""

#Usando GroupBy
data.groupby('Category').Category.count()

data.groupby('Category').Category.count().plot(kind='bar')

#Usando Countplot
sns.countplot(x='Category', data=data)
plt.show()

"""R3) Constam nesse dataset 5377 filmes e 2410 séries, totalizando

##Q4) Mostre todos os filmes lançados no ano 2000 e em 2015
"""

#Criando uma nova coluna
data['Year'] = data['Date_N'].dt.year
#Filtrando
data[(data['Category'] == 'Movie') & (data['Year']==2012)]

"""R4) Não foram lançados filmes no ano 2000, em 2012, foram lançados 3 filmes (Being Elmo: A Puppeteer's Journey, Casa de mi Padre e Kung Fu Panda: Holiday)

##Q5) Mostre apenas os titulos de séries que foram lançados apenas no Brasil.
"""

data[(data['Category']=='TV Show') & (data['Country']=='Brazil')] ['Title']

"""R5) Foram lançados 26 séries no Brasil.

##Q6) Mostre o top10 diretores, que trabalharam no maior número de séries e filmes para Netflix.
"""

#value_counts
data['Director'].value_counts().head(10)

"""R6) O Top10 diretores é:



1.Raúl Campos, Jan Suter    18
2.Marcus Raboy              16
3.Jay Karas                 14
4.Cathy Garcia-Molina       13
5.Jay Chapman               12
6.Youssef Chahine           12
7.Martin Scorsese           12
8.Steven Spielberg          10
9.David Dhawan               9
10.Hakan Algül               8
"""
