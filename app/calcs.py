import numpy as np
from scipy.stats import norm

def call_calc(s, k, r, sigma, q, t):
    """
    Returns the Call Price Calculated form the Black Scholes Option Pricing Model
    Inputs:
    s      -- Current stock price
    k      -- Strike price
    r      -- Risk free intrest (annualised)
    sigma  -- Implied volatility of asset
    q      -- Divident yeild of asset

    Outputs:
    C      -- Call price
    P      -- Put price
    """

    d1 = (np.log(s/k) + (r - q + sigma**2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - (sigma * np.sqrt(t))
    C = s * np.exp(-q * t) * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    CALL = round(C, 2)
    return CALL



def put_calc(s, k, r, sigma, q, t):
    """
    Returns the Put Price Calculated From the Black Scholes Option Pricing Model
    Inputs:
    s      -- Current stock price
    k      -- Strike price
    r      -- Risk free intrest (annualised)
    sigma  -- Implied volatility of asset
    q      -- Divident yeild of asset

    Outputs:
    C      -- Call price
    P      -- Put price
    """
    
    d1 = (np.log(s/k) + (r - q + sigma**2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - (sigma * np.sqrt(t))
    P = k * np.exp(-r * t) * norm.cdf(-d2) - s * np.exp(-q * t) * norm.cdf(-d1)

    PUT = round(P, 2)
    return PUT

def plot_values(direction, s, k, r, sigma, q, t):
    # Determining call or put
    if direction == "call":
        D = call_calc
    else:
        D = put_calc
    
    # Each set of T and S have 100 values
    NUMBER_OF_POINTS = 100
    
    # Both T and S are plotted logarythmically. This allows for greater datapoint density at closer to
    # expirey, where prices are most valatile

    # Getting S
    s_max = s * 1.4
    s_min = s * 0.6
    s_plots = np.logspace(np.log10(s_min), np.log10(s_max), NUMBER_OF_POINTS)
    
    # Getting T
    t_max = t
    t_min = 0.001 # (equiv to 1/4 of a working day)
    t_plots = np.logspace(np.log10(t_min), np.log10(t_max), NUMBER_OF_POINTS)

    # -- Create a matrix using the maths for the call/ put to get the thing --
    # Empty martix to fill (created at the same size of the length of x & y)
    matrix = np.zeros((len(s_plots), len(t_plots)))

    for i, S in enumerate(s_plots):
        for j, T in enumerate(t_plots):
            matrix[i, j] = D(s=S, t=T, k=k, sigma=sigma, q=q, r=r)


    return {
        "time_plot": t_plots.tolist(),
        "price_plot": s_plots.tolist(),
        "c_plot": matrix.tolist(),
        "s": s
    }
