* sort
~~~python
>> a=np.array([3,1,2])
>> sorted_index = np.argsort(a) # increasing order
[1,2,0]
>> sorted_index = np.argsort(-a) # decreasing order
[0,2,1]
~~~

*  statistics
~~~python
a = np.array([1,2,3])
>> np.max(a)
3
>> np.min(a)
1
>> np.mean(a, axis=0)
2
>> np.std(a)
0.8165
>> np.var(a)
0.6666
~~~

* random
~~~python
>> np.random.permutation(np.range(5))
[2,3,0,1,4]
~~~

* save/load
~~~python
import numpy as np
a=np.array([1,2,3])
np.save('some_directory.npy', a)
a=np.load('some_directory.npy')
~~~
~~~python
ls = [ np.array([1,2,3]),
      np.array([4,5,6]),
      np.array([7,8,9]) ]
np.savez('some_directory.npz', *ls)
npzfile=np.load('some_directory.npz')

>>> npzfile.files
['arr_0', 'arr_1', 'arr_2']
>>> npzfile['arr_0']
array([1,2,3])
>>> npzfile['arr_1']
array([4,5,6])
>>> npzfile['arr_2']
array([7,8,9])
~~~
