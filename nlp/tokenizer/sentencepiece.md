### 1. install
#### 1.1. python module
~~~
pip install sentencepiece
~~~
#### 1.2. C++ (from source)
On ubuntu 16.04 LTS (Xenial Xerus):
~~~
% sudo apt-get install libprotobuf9v5
% sudo apt-get install cmake pkg-config libprotobuf9v5 protobuf-compiler libprotobuf-dev libgoogle-perftools-dev 
% cd /path/to/sentencepiece
% mkdir build
% cd build
% cmake ..
% make -j $(nproc)
% sudo make install
% sudo ldconfig -v
~~~

### tokenize
~~~
import sentencepiece as spm
s = spm.SentencePieceProcessor()
s.Load('spm.model')
for n in range(5):
  s.SampleEncodeAsPiece('New York', -1, 0.1)
... 
['▁', 'N', 'e', 'w', '▁York']
['▁', 'New', '▁York']
['▁', 'New', '▁Y', 'o', 'r', 'k']
['▁', 'New', '▁York']
['▁', 'New', '▁York']
~~~
