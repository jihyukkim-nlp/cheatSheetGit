tutorial ref) 
- https://pytorch.org/tutorials/beginner/chatbot_tutorial.html
- 김성교수님(in English): https://www.youtube.com/watch?v=SKq-pmkekTk&list=PLlMkM4tgfjnJ3I-dbhO9JTw7gNty6o_2m
- Youtube, Neural Network Programming - Deep Learning with PyTorch: https://www.youtube.com/watch?v=v5cngxo4mIg&list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG
- Youtube, Deep Learning with PyTorch tutorial (packt video): https://www.youtube.com/watch?v=sQAoQZ5Q8wU&list=PLTgRMOcmRb3N0I4OxW7wZ7QHUjqrINoja
- Youtube, Pytorch for Beginners: https://www.youtube.com/watch?v=ZK6yi95XRvE&list=PLbMqOoYQ3Mxw1Sl5iAAV4SJmvnAGAhFvK


script file 을 만들어서 train/eval/vis를 진행
script file 에는 default argument 들이 있음 (argparse module 활용)

예)
> train.sh
~~~bash
python train.py --train --batch 32 --input_dir ../data/train.txt
~~~

> eval.sh
~~~bash
python eval.py --evaluation --batch 32 --input_dir ../data/test.txt
~~~
