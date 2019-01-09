# Evaluation Metrics

## Bleu
~~~python
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu
sentence_bleu(references=[[1,2,3,4,5,6]], hypothesis=[1,2,3,4,5,6], weights=(1,0,0,0))
corpus_bleu(references=[[1,2,3,4,5,6]], hypothesis=[1,2,3,4,5,6], weights=(1,0,0,0))
# weights=(1,0,0,0) means BLEU-1, weights=(0.25, 0.25, 0.25, 0.25) means BLEU-4
~~~
