import math
import numpy as np
# from matplotlib import pyplot as plt
# import seaborn as sns
import plotly.graph_objects as go

h = 6.63 * pow(10, -34)
k_B = 1.38 * pow(10, -23)
R= 8.3145 #j/mol/kelvin

temperature = np.linspace(298.18, 1500, 10000)
#np.array([298.18, 350, 375, 395 , 430 , 500 , 700 , 800 , 1000 , 1200])

#Ea = 34.2014  #(kcal/mol)   #claisen rearrangement activation function
Ea = 51.117  #(kcal/mol)
kcal_j = 4184
Ea_jol = Ea * kcal_j

factor = np.divide(-Ea_jol, (R*temperature))
exponential = np.exp(factor)
rate_const_lst = (k_B*temperature/h)*exponential


fig = go.Figure(data=go.Scatter(x=temperature, y=rate_const_lst, name="rate", line=dict(color='royalblue', width=4)))
    # Edit the layout
fig.update_layout(title='Rate Constant Vs temperature for SNi substitution using DFT(B3lyp)',
                  xaxis_title='Temperature (Kelvin)',
                  yaxis_title='Rate Constant')




fig.show()