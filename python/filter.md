~~~
parameters = filter(lambda p: p.requires_grad, model.parameters())
optimizer = torch.optim.Adadelta(parameters, lr=1.0, rho=0.9, eps=1e-6)
~~~
