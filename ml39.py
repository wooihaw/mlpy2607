# Clustering of non-spherical data points
from pandas import read_csv
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

X = read_csv("data/long_clusters.csv").values
km = KMeans(n_clusters=3, n_init=10).fit(X)
labels = GaussianMixture(n_components=3).fit_predict(X)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))
fig.suptitle('Clustering Comparison')
ax1.scatter(X[:, 0], X[:, 1])
ax1.set_title('Before clustering')
ax2.scatter(X[:, 0], X[:, 1], c=km.labels_)
ax2.set_title('k-means Clustering')
ax3.scatter(X[:, 0], X[:, 1], c=labels)
ax3.set_title('GMM Clustering')
plt.show()