# 1. port
## 1.1. port usage check
~~~
$ ps aux | grep redis
$ kill -9 [pid]
~~~
## 1.2. port settings
~~~
(server) 
$ redis-server --port [digits]
$ redis-cli -p [digits]
~~~


# 2. memory usage
## 2.1. memory check
~~~
$ info memory
~~~
## 2.2. number of keys
~~~
$ DBSIZE
~~~

# 3. saving RDB file
~~~
(client)
$ shutdown save
>> redis server 를 켤 때 RDB 파일이 자동으로 upload
~~~
