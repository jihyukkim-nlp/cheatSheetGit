script file 을 만들어서 train/eval/vis를 진행
script file 에는 default argument 들이 있음 (argparse module 활용)

예)
> train.sh
~~~bash
python --train -batch 32
~~~

> eval.sh
~~~bash
python --evaluation -batch 32
~~~
