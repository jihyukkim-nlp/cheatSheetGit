~~~
def to_var(x):
  return Variable(x).cuda() if torch.cuda.is_available() else Variable(x)
~~~
