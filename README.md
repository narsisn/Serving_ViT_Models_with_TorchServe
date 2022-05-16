# Serving ViT Models with TorchServe
Serving ViT Model for Feature Embedding using TorchServe Framework 

# Serving Steps:
**Step 1: Install the TorchServe and It's Requierments**

Please use the following URL to install and configure the TorchServe service on your system.
https://github.com/pytorch/serve/blob/master/README.md#serve-a-model

**Step 2: Saving the Model**

Run : Python3 model/model.py  
Note: Before running please define the model name at this file that has been hardcoded. 

TorchServe takes the following model artifacts: a model checkpoint file in case of torchscript or a model definition file and a state_dict file in case of eager mode.
TorchScript is a way to create serializable and optimizable models from PyTorch code. Any TorchScript program can be saved from a Python process and loaded in a process where there is no Python dependency.
Actually, torchScript is a common way to do inference with a trained model, an intermediate representation of a PyTorch model that can be run in Python as well as in a high performance environment like C++. TorchScript is actually the recommended model format for scaled inference and deployment.

**Step 3:  Creating the Handler File**

Customize the behavior of TorchServe by writing a Python script that you package with the model when you use the model archiver. TorchServe executes this code when it runs.

**Step 4: Exporting the .mar File (Torch Model Archiver)**

A key feature of TorchServe is the ability to package all model artifacts into a single model archive file. It is a separate command line interface (CLI), torch-model-archiver, that can take model checkpoints or model definition file with state_dict, and package them into a .mar file. This file can then be redistributed and served by anyone using TorchServe. It takes in the following model artifacts: a model checkpoint file in case of torchscript or a model definition file and a state_dict file in case of eager mode, and other optional assets that may be required to serve the model. The CLI creates a .mar file that TorchServe's server CLI uses to serve the models.

**Step 5: Deploying and Sending Requests**


Comming Soon ...
