~~~
from tqdm import tqdm
l = list('abcde')
for alpha in tqdm(l):
  # do something
d = {'a':1,'b':2,'c':3}
for alpha, number in tqdm(d, total=len(d)):
  # do something
~~~
