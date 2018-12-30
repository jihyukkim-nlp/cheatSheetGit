* binary cross entropy
~~~
self.criterion=torch.nn.functional.binary_cross_entropy
predict = torch.sigmoid(x)
label = Variable(x).float() # FloatTensor
self.criterion(predict, label)
~~~

* cross entropy
~~~
self.criterion = torch.nn.functional.cross_entroy
predict = torch.softmax(x, dim=1)
label = Variable(x).long() # LongTensor
self.criterion(predict, label)
~~~

* kl divergence
~~~
self.criterion = torch.nn.functional.kl_div
predict = torch.log_softmax(x, dim=1)
target = torch.softmax(x, dim=1)
self.criterion(predict, target)
~~~

#### search key
~~~
#loss #loss_function #cross_entroy #binary_cross_entropy #bce
#kld #kld_loss
~~~
