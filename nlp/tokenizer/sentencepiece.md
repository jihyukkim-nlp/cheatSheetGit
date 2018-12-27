### 1. install
#### 1.1. python module
~~~
pip install sentencepiece
~~~
#### 1.2. C++ (from source)
On ubuntu 16.04 LTS (Xenial Xerus):
~~~
$ git clone "https://github.com/google/sentencepiece.git"
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

### 2. train model
~~~
% spm_train --input=<input> --model_prefix=<model_name> --vocab_size=8000 --character_coverage=1.0 --model_type=<type>
~~~
* ```--input_sentence_size```: Note that ```spm_train``` loads only the first ```--input_sentence_size``` sentences (default value is 10M).
* ```--input```: one-sentence-per-line raw corpus file. No need to run tokenizer, normalizer or preprocessor. By default, SentencePiece normalizes the input with Unicode NFKC. You can pass a comma-separated list of files.
* ```--model_prefix```: output model name prefix. <model_name>.model and <model_name>.vocab are generated.
* ```--vocab_size```: vocabulary size, e.g., 8000, 16000, or 32000
* ```--character_coverage```: amount of characters covered by the model, good defaults are: 0.9995 for languages with rich character set like Japanse or Chinese and 1.0 for other languages with small character set.
* ```--model_type```: model type. Choose from unigram (default), bpe, char, or word. The input sentence must be pretokenized when using word type.
* ```--help```:  display all parameters for training.


### 3. tokenize
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

### 4. export vocabulary list
~~~
% spm_export_vocab --model=<model_file> --output=<output file>
~~~
```<output file>``` stores a list of vocabulary and emission log probabilities. The vocabulary id corresponds to the line number in this file.

### 5. put custom symbol into vocabulary
User defined symbol is handled as one piece in any context. If this symbol is included in the input text, this symbol is always extracted as one piece.
~~~
% spm_train --control_symbols=<s>,<\s> --user_defined_symbols=<user1>,<user2> --input=<input file> --model_prefix=<model file> --vocab_size=8000
~~~

# SentencePiece Python Wrapper

Python wrapper for SentencePiece with SWIG. This module wraps sentencepiece::SentencePieceProcessor class with the following modifications:
* Encode and Decode methods are re-defined as EncodeAsIds, EncodeAsPieces, DecodeIds and DecodePieces respectively.
* Support model training with SentencePieceTrainer.Train method.
* SentencePieceText proto is not supported.
* Added __len__ and __getitem__ methods. len(obj) and obj[key] returns vocab size and vocab id respectively.

## Build and Install SentencePiece
For Linux (x64/i686), macOS, and Windows(win32/x64) environment, you can simply use pip command to install SentencePiece python module.

```
% pip install sentencepiece
```

To build and install the Python wrapper from source, please install [SentencePiece C++](https://github.com/google/sentencepiece#c-from-source) and try the following commands:
```
% python setup.py build
% sudo python setup.py install
```

If you don’t have write permission to the global site-packages directory or don’t want to install into it, please try:
```
% python setup.py install --user
```

## Usage

### Segmentation
```
% python
>>> import sentencepiece as spm
>>> sp = spm.SentencePieceProcessor()
>>> sp.Load("test/test_model.model")
True
>>> sp.EncodeAsPieces("This is a test")
['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'est']
>>> sp.EncodeAsIds("This is a test")
[284, 47, 11, 4, 15, 400]
>>> sp.DecodePieces(['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'est'])
'This is a test'
>>> sp.NBestEncodeAsPieces("This is a test", 5)
[['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'est'], ['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 'te', 'st'], ['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 'te', 's', 't'], ['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'e', 'st'], ['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'es', 't']]
>>> for x in range(10):
...     sp.SampleEncodeAsPieces("This is a test", -1, 0.1)
...
['\xe2\x96\x81', 'T', 'h', 'i', 's', '\xe2\x96\x81', 'is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'e', 's', 't']
['\xe2\x96\x81T', 'h', 'is', '\xe2\x96\x81is', '\xe2\x96\x81', 'a', '\xe2\x96\x81', 't', 'est']
['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81', 'a', '\xe2\x96\x81', 't', 'e', 'st']
['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'e', 'st']
['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'e', 's', 't']
['\xe2\x96\x81T', 'h', 'is', '\xe2\x96\x81', 'i', 's', '\xe2\x96\x81a', '\xe2\x96\x81', 'te', 's', 't']
['\xe2\x96\x81This', '\xe2\x96\x81', 'is', '\xe2\x96\x81a', '\xe2\x96\x81', 'te', 's', 't']
['\xe2\x96\x81This', '\xe2\x96\x81', 'i', 's', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'e', 'st']
['\xe2\x96\x81This', '\xe2\x96\x81', 'is', '\xe2\x96\x81', 'a', '\xe2\x96\x81', 't', 'e', 'st']
['\xe2\x96\x81This', '\xe2\x96\x81', 'i', 's', '\xe2\x96\x81', 'a', '\xe2\x96\x81', 'te', 's', 't']
>>> sp.DecodeIds([284, 47, 11, 4, 15, 400])
'This is a test'
>>> sp.GetPieceSize()
1000
>>> sp.IdToPiece(2)
'</s>'
>>> sp.PieceToId('</s>')
2
>>> len(sp)
1000
>>> sp['</s>']
2
```

### Model Training
Training is performed by passing parameters of [spm_train](https://github.com/google/sentencepiece#train-sentencepiece-model) to  SentencePieceTrainer.Train() function.

```
>>> import sentencepiece as spm
>>> spm.SentencePieceTrainer.Train('--input=test/botchan.txt --model_prefix=m --vocab_size=1000')
unigram_model_trainer.cc(494) LOG(INFO) Starts training with : 
input: "test/botchan.txt"
model_prefix: "m"
model_type: UNIGRAM
..snip..
unigram_model_trainer.cc(529) LOG(INFO) EM sub_iter=0 size=1239 obj=10.4055 num_tokens=36256 num_tokens/piece=29.2623
unigram_model_trainer.cc(529) LOG(INFO) EM sub_iter=1 size=1239 obj=10.3187 num_tokens=36256 num_tokens/piece=29.2623
unigram_model_trainer.cc(529) LOG(INFO) EM sub_iter=0 size=1100 obj=10.5285 num_tokens=37633 num_tokens/piece=34.2118
unigram_model_trainer.cc(529) LOG(INFO) EM sub_iter=1 size=1100 obj=10.4973 num_tokens=37630 num_tokens/piece=34.2091
trainer_interface.cc(284) LOG(INFO) Saving model: m.model
trainer_interface.cc(293) LOG(INFO) Saving vocabs: m.vocab
>>>
```

## Python2/3 String/Unicode compatibility
Sentencepiece python wrapper accepts both Unicode string and legacy byte string.
The output string type is determined by the input string type.
The output type of IdToPiece/DecodeIds methods is *str*, but note that it is a legacy byte string in Python2 and Unicode string in Python3 respectively.

* Python2:
```
>>> sp.EncodeAsPieces('吾輩は猫である')
['\xe2\x96\x81', '\xe5\x90\xbe', '\xe8\xbc\xa9', '\xe3\x81\xaf', '\xe7\x8c\xab', '\xe3\x81\xa7\xe3\x81\x82\xe3\x82\x8b']
>>> sp.EncodeAsPieces(u'吾輩は猫である')
[u'\u2581', u'\u543e', u'\u8f29', u'\u306f', u'\u732b', u'\u3067\u3042\u308b']
>>> sp.EncodeAsPieces(u'吾輩は猫である'.encode('utf-8'))
['\xe2\x96\x81', '\xe5\x90\xbe', '\xe8\xbc\xa9', '\xe3\x81\xaf', '\xe7\x8c\xab', '\xe3\x81\xa7\xe3\x81\x82\xe3\x82\x8b']
>>> sp.IdToPiece(10)
'\xe3\x81\xab'
>>> type(sp.IdToPiece(10))
<type 'str'>
```

* Python3:
```
>>> sp.EncodeAsPieces('吾輩は猫である')
['▁', '吾', '輩', 'は', '猫', 'である']
>>> sp.EncodeAsPieces('吾輩は猫である'.encode('utf-8'))
[b'\xe2\x96\x81', b'\xe5\x90\xbe', b'\xe8\xbc\xa9', b'\xe3\x81\xaf', b'\xe7\x8c\xab', b'\xe3\x81\xa7\xe3\x81\x82\xe3\x82\x8b']
>>>
>>> sp.IdToPiece(10)
'に'
>>> type(sp.IdToPiece(10))
<class 'str'>
```
