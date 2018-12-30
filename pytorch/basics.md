1. creation
~~~
torch.from_numpy
torch.Tensor
torch.LongTensor
~~~

2. matrix multiplication
~~~
torch.mm
torch.bmm
~~~

3. type cast
~~~
a=torch.Tensor()
a.double()
~~~

4. module
~~~
class Model(nn.Module):
  def __init__(self, hyper_params):
    super(Model, self).__init__()
  def forward(self, x):
    return
~~~
