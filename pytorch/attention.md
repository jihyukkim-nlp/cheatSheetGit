#### with "for" loop

~~~
self.W = nn.Linear(hidden_size*2, hidden_size) # [key, query] > key
self.z = nn.Linear(hidden_size, 1) # key > score
for i in range(batch_size):
    dl = int(length[i]) # decoder_length for current instance
    key = memory_hidden[i] # num_memory*memory_length, hidden_size
    query = query_batch[i][:dl] # decoder_length, hidden_size (<eos> excluded)
    ml = key.size(0) # (num_memory*memory_length) for current instance

    key = key.unsqueeze(dim=0).repeat(dl, 1, 1) # dl, ml, hs
    query = query.unsqueeze(dim=1).repeat(1, ml, 1) # dl, ml, hs
    attention_score = self.z(torch.tanh(self.W(torch.cat([key, query], dim=2)))) # dl, ml, 1
    attention_score = F.softmax(attention_score, dim=1) # dl, ml, 1

    memory_reduced = torch.bmm(key.transpose(1,2), attention_score) # dl, hs, 1
    memory_reduced = memory_reduced.squeeze(dim=2) # dl, hs
    memory_reduced = memory_reduced.unsqueeze(dim=0) # 1, dl, hs


    if dl<decoder_length: # not maximum decoder size -> padding
        zero_padding_for_attention = self.IC.to_var(torch.zeros(decoder_length-dl, ml, 1))
        attention_score = torch.cat([attention_score, zero_padding_for_attention], dim=0) # decoder_length, num_memory*memory_length, 1
        zero_padding_for_hidden = self.IC.to_var(torch.zeros(1, decoder_length-dl, self.IC.hidden_size))
        memory_reduced = torch.cat([memory_reduced, zero_padding_for_hidden], dim=1)
    if ml<memory_length:
        zero_padding_for_attention = self.IC.to_var(torch.zeros(decoder_length, memory_length-ml, 1))
        attention_score = torch.cat([attention_score, zero_padding_for_attention], dim=1)

    memory_reduced_batch = memory_reduced if (memory_reduced_batch is None) else torch.cat([memory_reduced_batch, memory_reduced], dim=0)

    attention_score = attention_score.squeeze(dim=2)
    attention_score = attention_score.unsqueeze(dim=0) # 1, decoder_length, num_memory*memory_length
    if(memory_attention is None):
        memory_attention = attention_score
    else:
        memory_attention = torch.cat([memory_attention, attention_score], dim=0)
return (
    memory_reduced_batch, # batch_size, decoder_length, hidden_size
    memory_attention, # batch_size, decoder_length, num_memory*memory_length >> needed for copy mechanism
    ) 
~~~
