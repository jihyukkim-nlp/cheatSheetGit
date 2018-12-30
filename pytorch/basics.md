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
