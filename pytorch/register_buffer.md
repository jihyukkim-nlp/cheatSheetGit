you use register_buffer when:

you want a stateful part of your model that is not a parameter, but you want it in your state_dict
https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/batchnorm.py#L23-L24 864
registered buffers are Tensors (not Variables)
