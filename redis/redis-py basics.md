# redis-py basics
## 0. Install
~~~
$ pip install redis
>> import redis
>> r = redis.Redis(host='localhost', port=6379, db=0)
>> r.set(key1, value1)
~~~

