* lstm
~~~
self.lstm = torch.nn.LSTM(input_size=64, hidden_size=32, num_layer=1, bias=True, batch_first=True, bidirectional=True)
x >> batch_size, sequence_length, word_dimension
length >> list of lengths, length of list=batch_size
x_pack = torch.nn.utils.rnn.pack_padded_sequence(x, length, batch_first=True)
(h0, c0)=Variable(torch.zeros(2,2,batch_size,hidden_size)
hiddens, outs = self.lstm(x_pach, (h0, c0))
hiddens, length = torch.nn.utils.rnn.pad_packed_sequence(hiddens, batch_first=True)
~~~


#### search key
~~~
#rnn #lstm #gru
~~~
