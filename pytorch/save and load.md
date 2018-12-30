~~~
torch.save({
'model_name':model.name,
'param':model.state_dict(),
'epoch':epoch,
'train_loss':train_loss,
'dev_accuracy':dev_loss,
'test_accuracy':test_acc,
}, [file directory])
~~~

~~~
torch_file = torch.load([file directory .pth])
>> torch_file['model_name']
... 
~~~
