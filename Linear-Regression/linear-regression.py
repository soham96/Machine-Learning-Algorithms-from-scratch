from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def fit(x, y, epochs=50, learningrate=0.0001, initial_c=0, initial_m=0):
       print("Starting Linear Regression")

       N=len(x)

       for i in range(epochs):
              for j in range(N)
                     m+=-(2/N) * x * (y - ((m_current * x) + b_current))
                     c+=-(2/N) * (y - ((m_current * x) + b_current))
                     


if __name__ == '__main__':
       
       #fitting line y=mx+c
       df=pd.read_csv("cricket.txt", delimiter=",", header=None)
       df.columns=['Crickets', 'Temp']
       print(df.head())

       fit(initial_c=0, initial_m=0, learningrate=0.0001,x=df['Crickets'], y=df['Temp'],  epochs=50)