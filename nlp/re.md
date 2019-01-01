# Regular Expression
testing: https://regex101.com

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
* s (single line): dot matches newline
* i (insensitive): case insensitive match
* x (extended): ignore whitespace
* u (unicode): match with full unicode
* a (ascii): make escape sequences perform ASCII-only matching
