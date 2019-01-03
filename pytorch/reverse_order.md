# Reverse/Recover Order/Unsort
``` #recover_order #order_recovery #recovery #reverse_order #unsort```
~~~
sorted_idx      = np.argsort(-np.array(length))
recover_index   = np.zeros((len(sorted_idx)), dtype=np.int64)
for i in range(len(sorted_idx)): recover_index[sorted_idx[i]]=i
predict = np.array(predict)[recover_index] # recover original order
~~~
~~~python
x_sort_idx = np.argsort(-x_len)
x_unsort_idx = torch.LongTensor(np.argsort(x_sort_idx))
~~~
