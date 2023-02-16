import numpy as np
import matplotlib.pyplot as plt
import math


# set the simulation parameters
S0 = 100  # initial value of the asset
sigma = 0.1  # Vol
mu = 0.05 - 0.5**2   # drift Term
T = 1  # length of the simulation in years
dt = 1/365  # Time steps in days

# set the number of time steps and initialize the asset value array
n_steps = int(T / dt)
S = np.empty(n_steps + 1)
S[0] = S0

# Loop through the time steps and update the value of the asset value using the formula
for i in range (n_steps):
    dS = mu * S[i] * dt * sigma * S[i] * np.sqrt(dt) * np.random.normal()
    S[i + 1] = S[i] + dS



plt.title("Simulation of Stock price w/ Vol of " + str(sigma * 100) + "% and an initial value of " + str(S0) + " (Drift term =" + str(mu) + ")")
plt.xlabel("Time")
plt.ylabel("Price")
plt.plot(S)
plt.show()

