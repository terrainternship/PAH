
import os
import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

# Функции-утилиты для работы с категориальными данными
from tensorflow.keras import utils

# Класс для конструирования последовательной модели нейронной сети
from tensorflow.keras.models import Sequential

# Основные слои
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import SimpleRNN


from tensorflow.keras.models import load_model


DF_hi_korr = pd.read_csv('data_VVP.csv')
print(DF_hi_korr.shape)
print('Загрузка данных')

plt.plot(DF_hi_korr)
plt.show()
df = DF_hi_korr

x_test = (df-df.min())/(df.max()-df.min())

time_steps = 3
features = 4


# Инициализация массива x_test
x_test2 = np.zeros((x_test.shape[0] - time_steps + 1, time_steps, features))

# Заполнение массива x_test окнами размером time_steps
for i in range(x_test.shape[0] - time_steps + 1):
    x_test2[i] = x_test.iloc[i:i+time_steps].values


print('Загрузка модели')

model_v = load_model('model_rv.h5', compile=False)

print('Загрузка модели2')

model_v.summary()

print('Предсказание')
pref_dfv1 = model_v.predict(x_test2)
vvp = pref_dfv1 *12000
plt.plot(vvp)
plt.grid(True)
plt.show()
print('Предсказанные значения МЭП: ', vvp)

s = input ('Press Enter key: ')