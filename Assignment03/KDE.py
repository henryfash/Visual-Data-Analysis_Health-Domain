import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

# (a)
data = np.concatenate([np.random.normal(0, 2, 500), np.random.normal(9, 2, 1500)])[:, np.newaxis]
# (b)
plt.hist(data, 100)
plt.show()
# (c)
kde_gaussian = KernelDensity(kernel='gaussian', bandwidth=1.0).fit(data)
kde_linear = KernelDensity(kernel='linear', bandwidth=1.0).fit(data)
gaussian_score = kde_gaussian.score_samples(data)
linear_score = kde_linear.score_samples(data)
# visualize
# https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html
fig, ax = plt.subplots()
X_plot = np.linspace(-10, 20, 2000)[:, np.newaxis]
ax.plot(X_plot[:, 0], np.exp(linear_score), label="gaussian")
plt.show()
