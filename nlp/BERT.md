# BERT Pretrained Embedding

> ref) https://github.com/hanxiao/bert-as-service
> ref) https://github.com/google-research/bert

## Install
~~~bash
pip install bert-serving-server  # server
pip install bert-serving-client  # client, independent of `bert-serving-server`
~~~

## On Remote Server, e.g. ourkey
~~~bash
$ bert-serving-start -model_dir /hdd/models/BERT/uncased_L-24_H-1024_A-16/ -max_seq_len 61 -max_batch_size 512 -pooling_strategy NONE
~~~

## On Client
~~~python
from bert_serving.client import BertClient
bc = BertClient(ip="ip address of remote server")
bc.encode(['First do it', 'then do it right', 'then do it better'])
~~~ 
