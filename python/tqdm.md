~~~python
from tqdm import tqdm
ls = list('abcde')
for alpha in tqdm(ls):
  # do something
for alpha in tqdm(ls, ncols=50):
  # do something
for alpha in tqdm(ls, ncols=50, desc="ls progress bar"):
  # do something
  
d = {'a':1,'b':2,'c':3}
for alpha, number in tqdm(d, total=len(d)):
  # do something
 
ls = list('abcde')
for alpha in enumerate(tqdm(ls)):
  pass
~~~
