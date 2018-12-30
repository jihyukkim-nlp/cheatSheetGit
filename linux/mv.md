## mv [option] [src directory] [dst directory]

### option
* -b, --backup[=CONTROL] : 파일이 지워지기 전에 백업 파일을 만든다. '--suffix' 옵션을 지정하지 않으며 '~'를 붙여서 백업 파일 생성한다.
* -f, --force : 대상파일이 있더라도 파일을 강제(삭제 여부를 묻지 않고)로 삭제한다.
* -i, --interactive : 대상 파일이 있는 경우 덮어쓸 것인지 물어 본다.
* -strip-trailing-slashes : 옮길 대상(SOURCR)의 끝에 있는 슬러쉬('/')를 제거 하고 실행한다.
* -S, --suffix=SUFFIX : 지정된 접미사를 붙여서 덮어쓴다.
* -t, --target-directory=DIRECTORY : SOURCE의 모든 대상을 디렉토리로 옮긴다.
* -T, --no-target-directory : 옮길 대상을 일반파일로 취급한다.
* -u, --update : 대상파일보다 옮길 대상(SOURCE)이 최신 파일일 경우 업데이트한다. 기존의 대상 파일이 없을 경우 그냥 옮긴다.
* -v, --verbose : 파일 이동 과정을 출력한다.
* --help : 해당 명령어의 도움말을 보여주고 실행이 종료한다.
* --version : version 정보를 출력하고 실행이 종료한다.


### wild card
ex. 
``` mv *.gz ori_data ```


#### search key
~~~
#파일이동 #move
~~~
