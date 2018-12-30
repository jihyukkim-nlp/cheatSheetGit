# Initialize Parameters
torch version: 0.3.0 later on
### parameter declaration
~~~
self.linear = nn.Linear(512,256)
self.embedding = nn.Embedding(10, 256)
~~~

### initialization
~~~
torch.nn.init.xavier_uniform_(self.l1.weight)
torch.nn.init.uniform_(self.l1.weight, -0.01, 0.01)
torch.nn.init.constant_(self.l1.bias, 0)
torch.nn.init.xavier_uniform_(self.embedding)
~~~


### load pretrained vectors
e.g. word vectors
~~~
self.embed = nn.Embedding(100, 256)
word_vectors=np.load('word_vectors.npy')
self.embed.weight.data.copy_(torch.from_numpy(word_vectors.astype(np.float32)))
~~~

#### search key
~~~
#initialization #load_pretrained_vectors 
~~~
