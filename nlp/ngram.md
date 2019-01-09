# Ngram Extractor

> ref) https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/

~~~python
vect = CountVectorizer(ngram_range=(2, 2)).fit(corpus)
vect.vocabulary_
~~~
