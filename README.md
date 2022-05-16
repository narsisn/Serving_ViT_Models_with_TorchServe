# Serving ViT Models with TorchServe
Serving ViT Model for Feature Embedding using TorchServe Framework 

# Serving Steps:
**Step 1: Saving the Model**

Run : Python3 model/model.py  
Note: Befor ruuning please define the model name 

TorchServe takes  the following model artifacts: a model checkpoint file in case of torchscript or a model definition file and a state_dict file in case of eager mode.
TorchScript is a way to create serializable and optimizable models from PyTorch code. Any TorchScript program can be saved from a Python process and loaded in a process where there is no Python dependency.
Actually torchScript is an common way to do inference with a trained model, an intermediate representation of a PyTorch model that can be run in Python as well as in a high performance environment like C++. TorchScript is actually the recommended model format for scaled inference and deployment.




Comming Soon ...
