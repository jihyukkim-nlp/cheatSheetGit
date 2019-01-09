# Calculate TF-IDF scores

> ref) https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/
> ref) https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

~~~python
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
tfidf = TfidfVectorizer(vocabulary=vocab)
x_transformed = tfidf.fit_transform(x).toarray() # x is list of strings
~~~
