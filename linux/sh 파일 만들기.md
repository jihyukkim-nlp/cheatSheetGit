ref) http://gongdoo.tistory.com/241

> run.sh file
~~~bash
#! /bin/bash
echo "running bash script ... "
python3 train.py \
--model_name whoRU \
--dataset_dir /home/kimjihyeok/attend2u/data/caption_dataset \
--criterion cross_entropy \
--grad_clip 5 \
--L2_regularization 0 \
--num_epoch 20 \
--optimizer adadelta \
--learning_rate 1.0
~~~
