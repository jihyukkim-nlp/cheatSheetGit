"C++" env

### install
~~~bash
$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ make
~~~

### one document per one line

word token deliminator: " " (single white space)

### training
in fastText folder
~~~bash
$ ./fasttext skipgram -input "corpus directory" -output "model directory" -dim 100 -ws 3 -minCount 15
~~~


|parameter|	description|	default|
|---|---|---|
|input|	training file path	|mandatory|
|output|	output file path	|mandatory|
|verbose|	verbosity level	|2|
|minCount|	minimal number of word occurences	|5|
|minCountLabel|	minimal number of label occurences	|0|
|wordNgrams|	max length of word ngram	|1|
|bucket|	number of buckets	|2000000|
|minn|	min length of char ngram	|3|
|maxn|	max length of char ngram	|6|
|t|	sampling threshold	|0.0001|
|label|	labels prefix	|[]|
|lr|	learning rate	|0.05|
|lrUpdateRate|	change the rate of updates for the learning rate	|100|
|dim|	size of word vectors	|100|
|ws|	size of the context window	|5|
|epoch|	number of epochs	|5|
|neg|	number of negatives sampled	|5|
|loss|	loss function {ns, hs, softmax}	|ns|
|thread|	number of threads	|12|
|pretrainedVectors|	pretrained word vectors for supervised learning	|[]|
|saveOutput|	whether output params should be saved	|0|
|cutoff|	number of words and ngrams to retain	|0|
|retrain|	finetune embeddings if a cutoff is applied	|0|
|qnorm|	quantizing the norm separately	|0|
|qout|	quantizing the classifier	|0|
|dsub|	size of each sub-vector	|2|


### model loading
~~~python
#!pip install gensim
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('model directory')
~~~

### get vocabulary
~~~ python
vocab = model.index2word # class: list
~~~

### get word vectors
~~~python
wordvectors = []
for v in vocab:
	wordvectors.append(model.wv[v])
~~~

### similar words
~~~python
model.most_similar('영화', topn=30)
~~~
