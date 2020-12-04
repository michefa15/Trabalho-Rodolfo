# -*- coding: utf-8 -*-
"""Analise PETR4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12s8TTUPpdaY6OmS8SQluRIvyBz_k3nPo
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import drive

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.metrics import RootMeanSquaredError, MeanAbsoluteError, MeanAbsolutePercentageError
from tensorflow.keras.utils import plot_model

drive.mount("/content/drive", force_remount=True)

!ls /content/drive/MyDrive/Doutorado/Sistemas\ Hibridos

df_petr4 = pd.read_csv('/content/drive/MyDrive/Doutorado/Sistemas Hibridos/CotacoesPETR4certa.csv', sep=';', decimal=',')

df_petr4['Data'] = pd.to_datetime(df_petr4.Data, dayfirst=True)

df_petr4.dtypes

df_petr4.head()

df_petr4.Fechamento.plot()

df_petr4.describe()

"""Inicio do plano real: 27/02/1994
Por isso vamos pegar a partir de 95
"""

df_petr4 = df_petr4[df_petr4.Data>='1995-01-01']

df_petr4.describe()

df_petr4.head()

"""# Transformação dos dados
MinMaxScaler para transformar entre 0 e 1
"""

scaler = MinMaxScaler()

X = scaler.fit_transform(df_petr4[['Volume', 'Fechamento']].values)

df_petr4['volume_norm'] = X[:,0]
df_petr4['fechamento_norm'] = X[:,1]

df_petr4.head()

df_petr4.shape

df_petr4.volume_norm.shift(periods=1)

df_petr4.volume_norm.name

def create_sequence(df, column_name, lag=4):
  for i in range(lag):
    new_col_name = f'{column_name}_lag_{i+1}'
    df[new_col_name] = df[column_name].shift(periods= -(i+1))

create_sequence(df_petr4, 'volume_norm')
create_sequence(df_petr4, 'fechamento_norm')

df_petr4['y'] = df_petr4.fechamento_norm.shift(periods=-5)

df_petr4.head(6)

df_petr4.dropna(inplace=True)

X_volume = df_petr4[['volume_norm', 'volume_norm_lag_1', 'volume_norm_lag_2', 'volume_norm_lag_3','volume_norm_lag_4']].values
X_fechamento = df_petr4[['fechamento_norm', 'fechamento_norm_lag_1', 'fechamento_norm_lag_2', 'fechamento_norm_lag_3', 'fechamento_norm_lag_4']].values

X_volume.shape

X_fechamento.shape

X = np.stack((X_volume, X_fechamento), axis=2)

X.shape

y = df_petr4.y.values

"""[texto do link](https://)## Criação da divisão de treinamento e teste"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# Criação do modelo"""

model = Sequential()
model.add(LSTM(16, input_shape=(None,2,)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=[RootMeanSquaredError(), MeanAbsoluteError(), MeanAbsolutePercentageError()])

model.summary()

plot_model(model)

"""### Treinamento"""

history = model.fit(X_train, y_train, epochs=100, validation_split=0.1, batch_size=64)

history.history.keys()

"""# Metricas"""

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('MSE')
plt.ylabel('MSE')
plt.xlabel('epoch')
plt.legend(['train', 'val'])
plt.rcParams['figure.figsize'] = (5.0, 4.0)

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('RMSE')
plt.ylabel('RMSE')
plt.xlabel('epoch')
plt.legend(['train', 'val'])
plt.rcParams['figure.figsize'] = (5.0, 4.0)

plt.plot(history.history['mean_absolute_percentage_error'])
plt.plot(history.history['mean_absolute_percentage_error'])
plt.title('MAPE')
plt.ylabel('MAPE')
plt.xlabel('epoch')
plt.legend(['train', 'val'])

plt.rcParams['figure.figsize'] = (10.0, 10.0)

plt.subplot(221)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('MSE')
plt.ylabel('MSE')
plt.xlabel('epoch')
plt.legend(['train', 'val'])

plt.subplot(222)
plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('RMSE')
plt.ylabel('RMSE')
plt.xlabel('epoch')
plt.legend(['train', 'val'])

plt.subplot(223)
plt.plot(history.history['mean_absolute_error'])
plt.plot(history.history['val_mean_absolute_error'])
plt.title('MAE')
plt.ylabel('MAE')
plt.xlabel('epoch')
plt.legend(['train', 'val'])

plt.subplot(224)
plt.plot(history.history['mean_absolute_percentage_error'])
plt.plot(history.history['mean_absolute_percentage_error'])
plt.title('MAPE')
plt.ylabel('MAPE')
plt.xlabel('epoch')
plt.legend(['train', 'val'])

df_history = pd.DataFrame(history.history)

"""## Metricas para o conjunto de validação"""

df_history

df_history.tail(1)

"""## Metricas para o conjunto de teste

O conjunto de teste não foi visto pelo modelo em nenhum momento do treinamento. Só vai ser executado agora.
"""

y_pred = model.predict(X_test)

print('MSE:', mean_squared_error(y_test, y_pred))

print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred)))

print('MAE:', mean_absolute_error(y_test, y_pred))

def mape(y_true, y_pred):
  return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

print('MAPE:', mape(y_test, y_pred))

"""## Plot das previsões"""

plt.rcParams['figure.figsize'] = (10.0, 5.0)
plt.plot(df_petr4.Data, y)
plt.plot(df_petr4.Data, model.predict(X))

plt.legend(['Real', 'Predict'])

#plt.rcParams['figure.figsize'] = (4.0, 20.0)

