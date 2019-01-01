# Regular Expression
testing: https://regex101.com
ref: https://docs.python.org/3/library/re.html

## Basics
~~~
import re
abc=re.compile(r"abc")
s="abcdefg"
print(abc.sub("", s))
~~~

## Flags
* g (global): don't return after first match
* m (multi line): ^ and $ match start/end of line
* s (single line): dot matches newline(\n) (single line mode 로 newline 에 대한 . 의 exception 을 없앨 수 있음)
* i (insensitive): case insensitive match
* x (extended): ignore whitespace
* u (unicode): match with full unicode
* a (ascii): make escape sequences perform ASCII-only matching

## 11 Basic Single Character Meta Characters 
* \
* ^
* |
* .: matches all except new line
* $
* ?
* *
* +
* ()
* []
* {}

## More Meta Characters
* \d: 0-9
* \D: matches any character other than a decimal digit
* \w: a-zA-Z0-9 (matches any word character)
* \W: macthes any non-word character
* \s: matches any white-space characters ()
* \S: matches any non-white-space character

## Non-printable characters 

|\t|\n|\v|\r|\f|
|--|--|--|--|--|
|tab|new line| vertical tab| carriage return| form feed|
