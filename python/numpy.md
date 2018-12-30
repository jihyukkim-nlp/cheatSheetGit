* sort
~~~
>> a=np.array([3,1,2])
>> sorted_index = np.argsort(a) # increasing order
[1,2,0]
>> sorted_index = np.argsort(-a) # decreasing order
[0,2,1]
~~~

*  statistics
~~~
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
