from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
X, y = make_blobs(centers=3, cluster_std=2, random_state=42)
inertia = []
for k in range(2, 11):
    km = KMeans(n_clusters=k).fit(X)
    inertia.append(km.inertia_)

plt.plot(range(2, 11), inertia)
plt.xlabel('k')
plt.ylabel('Inertia')
plt.plot()
