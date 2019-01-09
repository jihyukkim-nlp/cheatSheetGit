# Calculate TF-IDF scores
~~~python
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer

tfidf = TfidfVectorizer(ngram_range=(1,5), max_features=500000)

data = train_data + val_data
x = [text for text, label in data]
x_transformed = tfidf.fit_transform(x)
~~~
