import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import norm

class Option:
    def __init__(self, S, K, T, r, sigma, option_type):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.option_type = option_type

    def d1(self):
        return (math.log(self.S / self.K) + (self.r + self.sigma ** 2 / 2) * self.T) / (self.sigma * math.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * math.sqrt(self.T)

    def price(self):
        if self.option_type == 'call':
            return self.S * norm.cdf(self.d1()) - self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2())
        elif self.option_type == 'put':
            return self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2()) - self.S * norm.cdf(-self.d1())
        else:
            return None

    def delta(self):
        if self.option_type == 'call':
            return norm.cdf(self.d1())
        elif self.option_type == 'put':
            return norm.cdf(self.d1()) - 1
        else:
            return None

    def gamma(self):
        return norm.pdf(self.d1()) / (self.S * self.sigma * math.sqrt(self.T))

    def vega(self):
        return self.S * norm.pdf(self.d1()) * math.sqrt(self.T)

    def theta(self):
        if self.option_type == 'call':
            return -(self.S * norm.pdf(self.d1()) * self.sigma / (2 * math.sqrt(self.T))) - self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2())
        elif self.option_type == 'put':
            return -(self.S * norm.pdf(self.d1()) * self.sigma / (2 * math.sqrt(self.T))) + self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2())
        else:
            return None

    def rho(self):
        if self.option_type == 'call':
            return self.T * self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2())
        elif self.option_type == 'put':
            return


# Input values for the option
S = 100
K = 100
T = 0.1
r = 0.25
sigma = 0.22
option_type = 'call'

# Create an instance of the Option class
option = Option(S, K, T, r, sigma, option_type)

# Display the price, delta, gamma, vega, theta and rho
print("Price: ", option.price())
print("Delta: ", option.delta())
print("Gamma: ", option.gamma())
print("Vega: ", option.vega())
print("Theta: ", option.theta())
print("Rho: ", option.rho())



asset_price_range = np.arange(K-50, K+50, 1)

# Calculate the payoff
if option_type == 'call':
    graph_payoff = np.maximum(asset_price_range- K, 0)
else:
    graph_payoff = np.maximum(K - asset_price_range, 0)


# Plot the payoff
plt.plot(asset_price_range, graph_payoff)
plt.xlabel('Stock Price')
plt.ylabel('Payoff')
plt.title('Option Payoff')
plt.show()

