import matplotlib.pyplot as plt
import numpy as np

# Return a number of random samples from the standard normal distribution
mu = 100
sigma = 25
x = np.random.normal(mu, sigma, 10000)
x = np.array(sorted(x))

# Equation for the PDF of a normal distribution
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.e ** (-((x - mu) ** 2) / (2 * sigma**2))

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set(xlim=(x.min(), x.max()), xlabel="x", ylim=(0, y.max()))
ax.text(
    0.7,
    0.8,
    r"$y = \frac{1}{\sigma \sqrt{2 \pi}} \ e^{-\frac{(x - \mu)^2}{2 \sigma^2}}$",
    transform=ax.transAxes,
    fontsize=17,
)

plt.show()
