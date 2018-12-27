### install
for linux
~~~
$ sudo apt-get install g++ openjdk-7-jdk python-dev python3-dev
$ pip3 install konlpy       # Python 3.x
~~~


### posTagging
~~~
>> from konlpy.tag import Kkma # or Hannanum, Komoran, Mecab, Okt, Twitter
>> kkma = Kkma()
>> kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.')
[질문,
 건의,
 건의사항,
 사항,
 깃헙,
 이슈,
 트래커]
>> kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^')
[(오류, NNG),
 (보고, NNG),
 (는, JX),
 (실행, NNG),
 (환경, NNG),
 (,, SP),
 (에러, NNG),
 (메세지, NNG),
 (와, JKM),
 (함께, MAG),
 (설명, NNG),
 (을, JKO),
 (최대한, NNG),
 (상세히, MAG),
 (!, SF),
 (^^, EMO)]
~~~
