### package install
~~~
$ tar zxvf aaa.tar.gz
$ cd aaa
$ python setup.py install
~~~
---------------------------------------
### get variable, method list ``` #unknown_library ```
~~~python
>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>> a=100
>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
>> __name__
'__main__'
>>> s="abc"
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
~~~

### single line code ``` ; and \ ```
~~~python
>> a=1;b=3
>> if a==1 and \
      b==3:
      print("yes!")
~~~

> NOTE) build-in data structure 는 모두 reference 로 참조 

### execute string statement ``` eval, exec, compile ``` 
~~~python
>> a=3
>> expr = "a+4" # statement is not allowed, e.g. "a=3"
>> eval(expr)
7
>> stmt = "a=a+3"
>> exec(stmt)
10
>> multiple_stmt = """
if a==10:
  print("is 10")
else:
  print("not 10") 
"""
>> exec(multiple_stmt)
is 10
~~~
> NOTE) compile function 

### print( , , , end=' ', sep=', ', file=[file descriptor])
> NOTE) import pprint; pprint() #complex print 

### Memory Management
#### reference count
~~~python
>> import sys
>> a=b=c=500
>> sys.getrefcount(a) #ref count including function call "getrefcount" (actual reference = return value - 1)
4 
~~~
#### identification
~~~python
>> a=b=500
>> id(a)
22675984
>> id(b)
22675984
>> a is b #compare address of object
True
>> a==b #compare value of object
True
~~~

### Iterator ``` 메모리관리와 연산의 효율성 증대, lazy evaluation ``` 
~~~python
>> i = iter(range(10))
>> next(i)
0
>> next(i)
1
~~~
> NOTE) generator ``` () rather than [] ```
~~~python
>> ((a+1) for a in range(100))
<generator object <genexpr> at 0x000000>
~~~
> lazy evaluation
---------------------------------------------------------------------
### 1. String
#### 1.1. slicing ``` [start:stop:step] ```
~~~python
>> s='abcd'
>> s[1:]
bcd
>> s[:-1]
abc
>> s[::2]
ac
>> s[::-1]
dcba
~~~
#### 1.2. method 
* len
* in
* upper, lower, capitalize, title
* startswith, endswith
* find, rfind, index, rindex
* count
* strip, lstrip, rstrip, replace
* split, lsplit, rsplit, join 
* center, ljust, rjust
* isdigit, isnumeric, isdecimal, isalpha, isalnum, islower, isupper, isspace
#### 1.3. operator ``` +, * ```
> NOTE) defining unicode characters "\uac00"='가'
#### 1.4. 한글 유니코드 자소 추출
한글 유니코드 = 0xAC00 + ((초성순서*21) + 중성순서)*28 + 종성순서
``` chr(0xd55c) == '한' ```
~~~python
def compose_hangul(cho, jung, jong):
  code = 0xac00 + ((cho*21)+jung)*28+jong
  return chr(code)
print(compose_hangul(18, 0, 4)) # result = '한'
~~~

* 초성: ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ
* 중성: ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ
* 종성: 없음(0) ㄱ(1), (ㄲ)(ㄱㅅ)(ㄴ)(ㄴㅈ)(ㄴㅎ)(ㄷ)(ㄹ)(ㄹㄱ)(ㄹㅁ)(ㄹㅂ)(ㄹㅅ)(ㄹㅌ)(ㄹㅍ)(ㄹㅎ)(ㅁ)(ㅂ)(ㅂㅅ)(ㅅ)(ㅆ)(ㅇ)(ㅈ)(ㅊ)(ㅋ)(ㅌ)(ㅍ)(ㅎ)
~~~python
def decompose_hangul(c):
  code=ord(c)-0xac00
  cho=code//(21*28)
  jung=(code-cho*21*28)//28
  jong=(cod-cho*21*28-jung*28)
  return cholist[cho], junglist[jung], jonglist[jong]
~~~

--------------------------------------------

### 2. List
#### 2.1. method
| | | | |
|-|-|-|-|
|append|insert|extend||
|index|count|||
|sort|reverse|||
|remove|pop|||
~~~python
>> s=[1,2,3]
>> s.append(5) # no return
[1,2,3,5]
>> s.insert(3,4) # no return
>> s
[1,2,3,4,5]
>> s.index(3)
2
>> s.count(2)
1
>> s.reverse() # no return
>> s
[5,4,3,2,1]
>> s.sort() # no return
>> s
[1,2,3,4,5]
>> s.sort(reverse=True) # no return
>> s
[5,4,3,2,1]
>> s.sort()
>> s.remove(5) # no return
>> s
[1,2,3,4]
>> s.extend([6,7]) 
[1,2,3,4,6,7]
>> s.pop(0) # now s=[2,3,4,6,7]
1
>> s.pop(1) # now s=[2,4,6,7]
3
~~~
#### 2.2. sort ```key attribute, sorted method```
~~~python
>> s = ['123','456','78']
>> s.sort(key=int, reverse=True) # compare after applying "int" built-in function
>> s
['789', '456', '123']
>> def mykey(a):
      return a%3
>> L=[1,5,3,9,8,4,2]
>> L.sort(key=mykey)
>> L
[3,9,1,4,5,8,2]
>> L=[1,5,3,9,8,4,2] # with lambda function
>> L.sort(key=lambda x: x%3)
>> L
[3,9,1,4,5,8,2]
>> newList=L.sorted() # no change for original list L
>> newList
[1,2,3,4,5,8,9]
>> L
[3,9,1,4,5,8,2]
~~~
#### 2.3. reversed
> NOTE) reversed function return iterator
~~~python
>> L=list('abc')
>> for c in L.reversed():print(c)
c
b
a
~~~
-----------------------------------------------------------------
### 3. Tuple
> NOTE) tuple 도 sequence 자료형이므로 ``` *, +, in, len, count, index ``` 등을 지원한다.
> NOTE) tuple 은 값을 변경할 수 없는데 값을 변경할 수 없으면 hashable 하기 때문에 검색이 빠르다.
#### 3.1. Packing, Unpacking
~~~python
>> t=1,2,"hellow" # packing
>> x,y,z=t # unpacking
~~~
- extended unpacking
~~~python
>> t = (1,2,3,4,5)
>> a, *b = t # * means rest of all
>> a
1
>> b
2,3,4,5  
~~~

#### 3.2. Using tuple as arguments
~~~python
def fn(a,b,c):
	return c,b,a
t=(1,2,3)
print(fn(*t))
~~~

#### 3.3. namedtuple()
~~~python
>>> from collections import namedtuple
>>> Circle = namedtuple('CircleNamedTuple', 'cx cy radius')
>>> Circle.__name__
'CircleNamedTuple'
>>> c1 = Circle(1.0, 2.0, 1.0)
>>> c2 = Circle(3.4, 2.2, 2.0)
>>> c1
CircleNamedTuple(cx=1.0, cy=2.0, radius=1.0)
>>> c2.cx, c2.cy, c2.radius
(3.4, 2.2, 2.0)
~~~
------------------------------------------------------------------------------
### 4. Set
> NOTE) sequential 자료형이 아니므로 indexing, slicing, sorting 을 지원하지 않는다.

#### 4.1. Instantiation
~~~python
>> a=set()   # using set()
>> a={1,2,3} # using {}
~~~

#### 4.2. Methods
| | | | |
|-|-|-|-|
|add|update|||
|discard|remove|clear|pop|
|intersection|union|difference|symmetric_difference|
|issuperset|issubsub|isdisjoint||
--------------------------------------------------------------------------------------
### 5. Dictionary
#### 5.1. Methods
| | | | |
|-|-|-|-|
|D.clear()|D.copy()|||
|D.get(key, [,x])|D.setdefault(key, [,x])|||
|D.update(D2)||||
|D.popitem()|D.pop(key)|||
### 5.2. IF statement
> NOTE) can be replaced by dictionary structure and get function
~~~python
>> order="spagetti"
>> menu={"spam":500, "ham":700, "egg":300}
>> price=menu.get(order, 0) #return 0 if there is no key for [order]
~~~
~~~python
#conditional function call
>> def add(a,b): return a+b
>> def sub(a,b): return a-b
>> a=10
>> {True:add, False:sub}[a>5](3,4)
7
~~~
