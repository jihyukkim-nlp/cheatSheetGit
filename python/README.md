### package install
~~~
$ tar zxvf aaa.tar.gz
$ cd aaa
$ python setup.py install
~~~

### single line code
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

### String
#### slicing ``` [start:stop:step] ```
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
#### method 
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
#### operator ``` +, * ```
> NOTE) defining unicode characters "\uac00"='가'
#### 한글 유니코드 자소 추출
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

### If statement
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

### Iterator ``` 메모리관리와 연산의 효율성 증대, lazy evaluation ``` 
~~~python
>> i = iter(range(10))
>> next(i)
0
>> next(i)
1
~~~
