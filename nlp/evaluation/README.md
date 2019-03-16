# Evaluation Metrics

## Bleu
~~~python
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu
sentence_bleu(references=[[1,2,3,4,5,6]], hypothesis=[1,2,3,4,5,6], weights=(1,0,0,0))
corpus_bleu(list_of_references=[ [[1,2,3,4,5,6]], [[ ... ]] ], hypotheses=[ [1,2,3,4,5,6], [...] ], weights=(1,0,0,0))
# weights=(1,0,0,0) means BLEU-1, weights=(0.25, 0.25, 0.25, 0.25) means BLEU-4
# references: multiple target sequences
# hypothesis: predicted(or generated) sequences
~~~


## ROUGE
 open source ROUGE-1.5.5
 https://github.com/bheinzerling/pyrouge
 
 additional links:
 Setup: https://poojithansl7.wordpress.com/2018/08/04/setting-up-rouge/
 General Procedure: https://ireneli.eu/2018/01/11/working-with-rouge-1-5-5-evaluation-metric-in-python/
 WordNet Exception: https://github.com/bheinzerling/pyrouge/issues/8
 
