* only for tensor input
~~~
def to_var(x):
  return Variable(x).cuda() if torch.cuda.is_available() else Variable(x)
def to_var_fixed(x):
  return Variable(x, requires_grad=False).cuda() if torch.cuda.is_available() else Variable(x, requires_grad=False)
~~~

* for generic input (tensor, list, ndarray)
~~~
def to_var(x):
  if isinstance(x, list):
    if isinstance(x[0], int):
      return Variable(torch.LongTensor(x)).cuda() if torch.cuda.is_available() else Variable(torch.LongTensor(x))
    elif isinstance(x[0], float):
      return Variable(torch.Tensor(x)).cuda() if torch.cuda.is_available() else Variable(torch.Tensor(x))
    else:
      raise Exception
  elif isinstance(x, (np.ndarray, np.generic)):
    return Variable(torch.from_numpy(x)).cuda() if torch.cuda.is_available() else Variable(torch.from_numpy(x))
  else:
    return Variable(x).cuda() if torch.cuda.is_available() else Variable(x)
def to_var_cpu(x):
  if isinstance(x, list):
    if isinstance(x[0], int):
      return Variable(torch.LongTensor(x))
    elif isinstance(x[0], float):
      return Variable(torch.Tensor(x))
    else:
      raise Exception
  elif isinstance(x, (np.ndarray, np.generic)):
    return Variable(torch.from_numpy(x))
  else:
    return Variable(x)
~~~
