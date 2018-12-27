## tSNE
~~~
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

model = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300, learning_rate=100)
transformed = model.fit_transform(feature)

xs = transformed[:,0]
ys = transformed[:,1]
plt.scatter(xs,ys,c=labels)

plt.show()
~~~

## PCA
~~~
from sklearn.decomposition import PCA

model = PCA(n_components=2)
transformed = model.fit_transform(feature)

xs = transformed[:,0]
ys = transformed[:,1]
plt.scatter(xs,ys,c=labels)

plt.show()
~~~
