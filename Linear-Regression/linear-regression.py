from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def fit(x, y, epochs=50, learningrate=0.0001, initial_b=0, initial_m=0):
       print("Starting Linear Regression")

if __name__ == '__main__':
       
       #fitting line y=mx+b
       initial_b=0
       initial_m=0
       learningrate=0.0001
       epochs=50
       df=pd.read_csv("cricket.txt", delimiter=",", header=None)
       df.columns=['Crickets', 'Temp']
       print(df.head())

       fit(initial_b=initial_b, initial_m=initial_m, learningrate=learningrate,x=df['Crickets'], y=df['Temp'],  epochs=epochs)