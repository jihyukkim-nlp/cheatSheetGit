tutorial ref) 
- https://pytorch.org/tutorials/beginner/chatbot_tutorial.html
- 김성교수님(in English): https://www.youtube.com/watch?v=SKq-pmkekTk&list=PLlMkM4tgfjnJ3I-dbhO9JTw7gNty6o_2m
- Youtube, Neural Network Programming - Deep Learning with PyTorch: https://www.youtube.com/watch?v=v5cngxo4mIg&list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG
- Youtube, Deep Learning with PyTorch tutorial (packt video): https://www.youtube.com/watch?v=sQAoQZ5Q8wU&list=PLTgRMOcmRb3N0I4OxW7wZ7QHUjqrINoja
- Youtube, Pytorch for Beginners: https://www.youtube.com/watch?v=ZK6yi95XRvE&list=PLbMqOoYQ3Mxw1Sl5iAAV4SJmvnAGAhFvK

-----------------------------------
script file 을 만들어서 train/eval/vis를 진행
script file 에는 default argument 들이 있음 (argparse module 활용)

예)
> train.sh
~~~bash
#! /bin/bash
echo "running bash script ... \"train.sh\" "
python train.py \
--train \
--batch 32 \
--input_dir ../data/train.txt
~~~

> eval.sh
~~~bash
#! /bin/bash
echo "running bash script ... \"eval.sh\""
python eval.py \
--evaluation \
--batch 32 \
--input_dir ../data/test.txt
~~~
-----------------------------------

## torch.max
~~~python
>>> a = torch.Tensor([1,2,3])
>>> torch.max(a) # values, indices
>>> (3,), (2,)
~~~

## torch.sort()
~~~python
>>> x = torch.randn(3, 4)
>>> sorted, indices = torch.sort(x)
>>> sorted
tensor([[-0.2162,  0.0608,  0.6719,  2.3332],
        [-0.5793,  0.0061,  0.6058,  0.9497],
        [-0.5071,  0.3343,  0.9553,  1.0960]])
>>> indices
tensor([[ 1,  0,  2,  3],
        [ 3,  1,  0,  2],
        [ 0,  3,  1,  2]])

>>> sorted, indices = torch.sort(x, 0)
>>> sorted
tensor([[-0.5071, -0.2162,  0.6719, -0.5793],
        [ 0.0608,  0.0061,  0.9497,  0.3343],
        [ 0.6058,  0.9553,  1.0960,  2.3332]])
>>> indices
tensor([[ 2,  0,  0,  1],
        [ 0,  1,  1,  2],
        [ 1,  2,  2,  0]])
~~~

## torch.topk(input, k, dim=None, largest=True, sorted=True, out=None) -> (Tensor, LongTensor)
~~~python
>>> x = torch.arange(1., 6.)
>>> x
tensor([ 1.,  2.,  3.,  4.,  5.])
>>> torch.topk(x, 3)
(tensor([ 5.,  4.,  3.]), tensor([ 4,  3,  2]))
~~~

## Cuda 확인
~~~python
>>> a=torch.Tensor([1])
>>> a.is_cuda
False
>>> b=torch.Tensor([1]).cuda()
>>> b.is_cuda
True
>>> c = torch.Tensor([2]).to(device='cuda')
>>> c
tensor([ 2.], device='cuda:0')
>>> c.is_cuda
True
>>> d = torch.Tensor([2]).to(device='cpu')
>>> d
tensor([ 2.])
>>> d.is_cuda
False
~~~

## Cuda Debugging
~~~python
CUDA_LAUNCH_BLOCKING=1 python3 train.py
~~~

## contiguous
~~~python
is_contiguous()
contiguous()
~~~
~~~
