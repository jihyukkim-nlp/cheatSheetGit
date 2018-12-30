~~~
>> cat [options] [filenames]
>> cat [filename1] [filename2] [filename2] ...
show [filename#] on current terminal
>> cat [filename] | more
화면에 보여질 내용이 너무 많을 때 편하다.
>> cat [file(s)] > [new_file]
파일들을 순서대로 이어붙여서 새로운 파일을 만든다. 새로운 파일이 이미 존재하는 파일이라면 덮어쓴다.
>> cat [file] >> [dst file]
[file] 을 [dst file]에 이어붙인다.
>> cat > [new_file]
터미널 입력으로 내용을 입력할 수 있고 Ctrl-d 를 입력하면 새로운 내용이 저장된 새로운 파일이 만들어진다.
~~~

### options
* -b: 줄번호를 화면 왼쪽에 나타낸다. 비어있는 행은 제외한다.
* -e: 제어 문자를 ^ 형태로 출력하면서 각 행의 끝에 $를 추가한다.
* -n: 줄번호를 화면 왼쪽에 나타낸다. 비어있는 행도 포함한다.
* -s: 연속되는 2개이상의 빈 행을 한행으로 출력한다.
* -v: tab과 행 바꿈 문자를 제외한 제어 문자를 ^ 형태로 출력한다.
* -E: 행마다 끝에 $ 문자를 출력한다.
* -T: 탭(tab) 문자를 출력한다.
* -A: -vET 옵션을 사용한 것과 같은 효과를 본다.



#### search key
~~~
#파일생성 #create #make #파일보기 #show
~~~
