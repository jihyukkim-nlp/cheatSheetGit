
# argparse

## 1. instantiation
~~~python
import argparse
parser = argparse.ArgumentParser(description=" ")
~~~

## 2. arguments
~~~python
parser.add_argument("first", type=int)
parser.add_argument("second", type=float)
parser.add_argument("third") #default type is 'str'
parser.add_argument("fourth", nargs=2)
parser.add_argument("fifth", nargs="*") # *(0 or more), ?(0 or 1), +(1 or more)
args = parser.parse_args()
print("first={}, second={}, third={}, fourth={}, fifth={}".format(\
	args.first, args.second, args.third, args.fourth, args.fifth))
~~~
~~~bash
$ python argparse_example.py 1 2.3 "some string" one two dot dot dot
first=1, second=2.3, third=some string, fourth=['one' 'two'], fifth=['dot','dot','dot']
~~~

## 3. Attributes
### 3.1. action
~~~python
parser.add_argument('-true', action="store_true", default=False)
parser.add_argument('-false', action="store_false", default=True)
parser.add_argument('-integer', action="store_const", const="1")
parser.add_argument('-listappend', action="append")
parser.add_argument('-listappendconst', action="append_const", const="1")
~~~
### 3.2. dest
~~~python
parser.add_argument("-r", dest="rate", type=float, default=1.0) # value saved in name "rate"
~~~
### 3.3. version
~~~python
parser.add_argument("--version", action="version", version="v2.3")
~~~

