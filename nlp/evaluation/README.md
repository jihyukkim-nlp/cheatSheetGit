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
~~~python
import sys
sys.path.extend(['/home/kimjihyeok/pyrouge/'])
from pyrouge import Rouge155

basedir = '/home/somedirectory'
corpusdir = os.path.join(basedir, 'corpus')
syspath = os.path.join(corpusdir, 'sys') // generated text
refpath = os.path.join(corpusdir, 'ref') // target text

rouge = Rouge155()
rouge.system_dir = os.path.join(corpusdir, 'sys/')
rouge.model_dir = os.path.join(corpusdir, 'ref/')
rouge.system_filename_pattern = 'system.(\d+).txt'
rouge.model_filename_pattern = 'model.d.#ID#.txt'
output = rouge.convert_and_evaluate()
output_dict = rouge.output_to_dict(output)
~~~
~~~bash
>> type(output)
 'dict'
>> output_dict.keys()
 dict_keys(['rouge_1_recall', 'rouge_1_recall_cb', 'rouge_1_recall_ce', 'rouge_1_precision', 'rouge_1_precision_cb', 'rouge_1_precision_ce', 'rouge_1_f_score', 'rouge_1_f_score_cb', 'rouge_1_f_score_ce', 'rouge_2_recall', 'rouge_2_recall_cb', 'rouge_2_recall_ce', 'rouge_2_precision', 'rouge_2_precision_cb', 'rouge_2_precision_ce', 'rouge_2_f_score', 'rouge_2_f_score_cb', 'rouge_2_f_score_ce', 'rouge_3_recall', 'rouge_3_recall_cb', 'rouge_3_recall_ce', 'rouge_3_precision', 'rouge_3_precision_cb', 'rouge_3_precision_ce', 'rouge_3_f_score', 'rouge_3_f_score_cb', 'rouge_3_f_score_ce', 'rouge_4_recall', 'rouge_4_recall_cb', 'rouge_4_recall_ce', 'rouge_4_precision', 'rouge_4_precision_cb', 'rouge_4_precision_ce', 'rouge_4_f_score', 'rouge_4_f_score_cb', 'rouge_4_f_score_ce', 'rouge_l_recall', 'rouge_l_recall_cb', 'rouge_l_recall_ce', 'rouge_l_precision', 'rouge_l_precision_cb', 'rouge_l_precision_ce', 'rouge_l_f_score', 'rouge_l_f_score_cb', 'rouge_l_f_score_ce', 'rouge_w_1.2_recall', 'rouge_w_1.2_recall_cb', 'rouge_w_1.2_recall_ce', 'rouge_w_1.2_precision', 'rouge_w_1.2_precision_cb', 'rouge_w_1.2_precision_ce', 'rouge_w_1.2_f_score', 'rouge_w_1.2_f_score_cb', 'rouge_w_1.2_f_score_ce', 'rouge_s*_recall', 'rouge_s*_recall_cb', 'rouge_s*_recall_ce', 'rouge_s*_precision', 'rouge_s*_precision_cb', 'rouge_s*_precision_ce', 'rouge_s*_f_score', 'rouge_s*_f_score_cb', 'rouge_s*_f_score_ce', 'rouge_su*_recall', 'rouge_su*_recall_cb', 'rouge_su*_recall_ce', 'rouge_su*_precision', 'rouge_su*_precision_cb', 'rouge_su*_precision_ce', 'rouge_su*_f_score', 'rouge_su*_f_score_cb', 'rouge_su*_f_score_ce'])
~~~
