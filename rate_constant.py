import math
import numpy as np
# from matplotlib import pyplot as plt
# import seaborn as sns
import plotly.graph_objects as go

h = 6.63 * pow(10, -34)
k_B = 1.38 * pow(10, -23)

transition_pot =2
pot =1
def get_transmission_coefficient(trans_im_freq, T):

    alpha = (2* (math.pi))/(trans_im_freq*h)
    beta = 1/(k_B * T)

    if alpha >= beta:
        expr = (beta * math.pi) / alpha
        expr2 = beta/(alpha - beta)
        expr3 = (beta - alpha) * (transition_pot - pot)
        transmission_coeff = expr/math.sin(expr) - expr2 * math.exp(expr3)
    else:
        factor = beta/(beta - alpha)
        factor2 = (beta - alpha) * (transition_pot - pot)
        transmission_coeff = factor * ( math.exp(factor2) -1)

    return transmission_coeff

def calculate_rate_constant(T, act_ener, trans_im_freq):
    """
     Calculate rate of reaction using Variational Transition State Theory
    """
    c_0 = 1
    thermal_energy = k_B * T
    trans_coeff = get_transmission_coefficient(trans_im_freq, T)
    act_ener = 20* thermal_energy
    factor = -(act_ener/thermal_energy)

    rate_const_fact  = trans_coeff * (thermal_energy/(c_0*h))
    rate_const = rate_const_fact * math.exp(factor)
    return rate_const

if __name__ == '__main__':
    lower = 298
    higher = 1200
    #specifications for claisen rearrangement
    transition_state_imaginary_freq = 2.7 *pow(10, 13)
    #activation_energy = 143098.6576
    temperature = [298.18, 350, 375, 395 , 430 , 500 , 700 , 800 , 1000 , 1200]
    activation_energy = 143098.5/(6.023 * pow(10,23))
    rate_const_lst = [ ]
    for temp in range(lower, higher, 10):
        rate_const = calculate_rate_constant(temp,activation_energy, transition_state_imaginary_freq)
        rate_const_lst.append(rate_const)

    fig = go.Figure(data=go.Scatter(x=temperature, y=rate_const_lst, name="rate", line=dict(color='royalblue', width=4)))
    # Edit the layout
    fig.update_layout(title='Rate Constant Vs temperature for Claisen Rearrangement using DFT(B3lyp)',
                      xaxis_title='Temperature (Kelvin)',
                      yaxis_title='Rate Constant')




    fig.show()

    #############GIBBS ################
    #gibbs_free_energy = [101.309, 96.878, 94.645, 92.814 , 89.513 , 82.543 , 59.988 , 47.313 , 19.390 , -11.382]
    # fig = go.Figure(data=go.Scatter(x=temperature, y=gibbs_free_energy, name="gibbs", line=dict(color='royalblue', width=4)))
    # # Edit the layout
    # fig.update_layout(title='Gibbs Free Energy Vs temperature for Claisen Rearrangement using DFT(B3lyp)',
    #                   xaxis_title='Temperature (Kelvin)',
    #                   yaxis_title='Gibbs Free Energy (kcal/mole)')
    #
    #
    #
    #
    # fig.show()

