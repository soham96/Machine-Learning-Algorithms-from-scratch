from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def calc_error(m, c, x, y):
       
       totalError=0

       for i in range(len(x)):
              totalError += (y[i] - (m * x[i] + c)) ** 2

       return totalError/float(len(x))

def fit(x, y, epochs=50, learningrate=0.0001, initial_c=0, initial_m=0):
       print("Starting Linear Regression")

       N=len(x)
       new_m=initial_m
       new_c=initial_c
       m=0
       c=0


       for i in range(epochs):
              for j in range(N):
                     m+= (-(2/float(N)) * x[j] * (y [j]- ((new_m * x[j]) + new_c)))
                     c+=(-(2/float(N)) * (y [j]- ((new_m * x[j]) + new_c)))
              new_m=new_m-(m*learningrate)
              new_c=new_c-(c*learningrate)
              m=0
              c=0
              error=calc_error(new_m, new_c, x, y)
              print("For Epoch {0} : slope={1} and y-intercept={2}".format(i, new_m, new_c))
              print("Mean Square Error = {0} \n".format(error))



if __name__ == '__main__':
       
       #fitting line y=mx+c
       df=pd.read_csv("cricket.txt", delimiter=",", header=None)
       df.columns=['Crickets', 'Temp']
       print(df.head())

       fit(initial_c=0, initial_m=0, learningrate=0.0001,x=df['Crickets'], y=df['Temp'],  epochs=100)