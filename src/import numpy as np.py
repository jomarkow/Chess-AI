import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate some example data (replace this with your data)
np.random.seed(0)
X = np.random.rand(100, 2) * 10  # Example: 100 points in 2D space

# Choose the number of clusters (you may need to tune this)
n_clusters = 2

# Create a K-Means clustering model
kmeans = KMeans(n_clusters=n_clusters, random_state=0)

# Fit the model to your data
kmeans.fit(X)

# Get cluster assignments for each data point
labels = kmeans.labels_

# Plot the data points with color-coded clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, linewidths=3, color='r')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('K-Means Clustering')
plt.show()
