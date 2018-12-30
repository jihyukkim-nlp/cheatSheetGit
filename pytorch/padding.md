~~~
 def add_pad(self, sentences, lengths):
      maxlen = np.max(lengths)
      padded_sentences = []
      for i, x in enumerate(sentences):
          if lengths[i] < maxlen : padded_sentences.append([int(w) for w in x]+[0]*(maxlen-lengths[i]))
          else: padded_sentences.append([int(w) for w in x])
      return padded_sentences
~~~
