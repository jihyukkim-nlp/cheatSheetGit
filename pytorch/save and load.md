~~~
torch.save({
'model_name':model.name,
'state_dict':model.state_dict(),
'epoch':epoch,
'train_loss':train_loss,
'dev_accuracy':dev_loss,
'test_accuracy':test_acc,
}, [file directory])
~~~

~~~
torch_file = torch.load([file directory .pth])
state_dict = torch_file['state_dict']
for name, param in state_dict.items():
  model.state_dict[name].copy_(param)
... 
~~~
