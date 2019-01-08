# tensorboardX

> ref) https://tensorboardx.readthedocs.io/en/latest/tutorial.html#what-is-tensorboard-x

## Install
~~~python
pip install tensorboard
pip install tensorboardX
~~~

## Basic Usage (Loss logging)
~~~python
from tensorboardX import SummaryWriter
writer = SummaryWritter(log_dir=[logging_directory])
writer.add_scalar('loss', loss, global_step)
writer.close()
~~~
~~~bash
>>> cd [logging_directory]
>>> tensorboard --logdir='./'
~~~
