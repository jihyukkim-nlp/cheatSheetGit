## 1. creation
~~~
torch.from_numpy
torch.Tensor
torch.LongTensor
~~~

## 2. matrix multiplication
~~~
torch.mm
torch.bmm
~~~

## 3. type cast
~~~
a=torch.Tensor()
a.double()
~~~

## 4. module
~~~
class Model(nn.Module):
  def __init__(self, hyper_params):
    super(Model, self).__init__()
  def forward(self, x):
    return
~~~

## 5. vector/matrix manipulation
### 5.1. stack
~~~
>> a = torch.Tensor([1,2,3]) # 3,
>> b = torch.Tensor([4,5,6]) # 3,
>> c = torch.stack([a,b], dim=0) # 2,3 
>> c
[[1,2,3],
 [4,5,6]] 
~~~
### 5.2. scatter_add_
~~~
word_distribution # batch_size, decoder_length, vocab_size
encoder_word_indices # batch_size, encoder_length
encoder_attention # batch_size, decoder_length, encoder_length
word_distribution = word_distribution.scatter_add_(2, encoder_word_indices, encoder_attention)
~~~
#### search key
~~~
#pointer_network #ptr #copying_mechanism #copy
~~~
