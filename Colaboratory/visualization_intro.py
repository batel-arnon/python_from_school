# -*- coding: utf-8 -*-
"""Visualization intro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tcy_OOAdabN83uC3P1QGOP6R5j7yWo5e
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = [4,4,5,5,5,5,6,6,7,5,8,8,5,9]
y = [3,1,2,3,3,3,3,4,2,1,2,5,3,4]
plt.plot(y)
plt.plot(y,'og')

plt.show()
plt.plot(x,y)
plt.plot(x,y,'or')

df = pd.read_csv('/content/drive/MyDrive/Iris.csv')
sns.scatterplot(data=df, x='SepalLengthCm', y='PetalLengthCm', hue='Species')

df = pd.read_csv('/content/drive/MyDrive/Iris.csv')
df.drop('Id', axis=1, inplace=True)
sns.pairplot(data=df,hue='Species')

#excercise:
sinValues = [0,1,0,-1,0,1,0,-1]
plt.plot(sinValues)
plt.plot(sinValues,'og')
plt.show()

df = pd.read_csv('/content/drive/MyDrive/Iris.csv')
sns.scatterplot(data=df[df['Species'] != 'Iris-versicolor'], x='SepalLengthCm', y='PetalLengthCm', hue='Species')

xor = [[0,0,False],
       [0,1,True],
       [1,0,True],
       [1,1,False]]
head = ['X', 'Y', 'trueValues']
df = pd.DataFrame(xor,columns=head)
sns.scatterplot(data = df, x = 'X', y = 'Y', hue='trueValues')