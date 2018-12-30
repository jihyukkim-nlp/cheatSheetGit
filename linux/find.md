## 1. find file
### 1.1. starting from current directory
~~~
find -name "filename"
~~~

### 1.2. from root
~~~
find / -name "filename"
~~~

### 1.3. list output
~~~
find -name "filename" -ls
~~~

## 2. find directory
~~~
find -name "directory name" -type d
~~~

## 2. grep
파일 내용 검색
~~~
grep -r "string" ./*
~~~
현재 디렉토리에서 시작해서 하위디렉토리 모두(-r)(recursive) 에서 "string" 이 있는 파일들을 찾아라


#### search key
~~~
#find #search #파일찾기 #파일검색 #파일내용
~~~
