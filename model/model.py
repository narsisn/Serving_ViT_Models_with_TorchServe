import os 
import torch 
from PIL import Image
import numpy as np
import requests

from transformers import CLIPVisionModel, AutoTokenizer, CLIPConfig, CLIPFeatureExtractor



class SaveModel:
    def __init__(self, model_path="", checkpoint_path="", image_url=""):
        self.checkpoint_path = checkpoint_path
        self.model_path = model_path
        self.image_url = image_url
    
    def load_model(self):

        config = CLIPConfig.from_pretrained(self.model_path)
        config.vision_config.torchscript =True
        vision_encoder = CLIPVisionModel.from_pretrained(self.model_path, config=config.vision_config )
        return vision_encoder

    def save_model(self,model):
        '''
        # Reload traced model and compare outputs to original one
        loaded_model = torch.jit.load("traced_vit.pt")
        loaded_model.eval()
        traced_outputs = loaded_model(**inputs)
        assert np.allclose(
            original_outputs[0].detach().numpy(), traced_outputs[0].detach().numpy()
        )
        '''
        feature_extractor = CLIPFeatureExtractor.from_pretrained(self.model_path)
        image = Image.open(requests.get(self.image_url, stream=True).raw)
        inputs = feature_extractor(images=image, return_tensors="pt")
        original_outputs = model(**inputs)
        traced_model = torch.jit.trace(model, [inputs["pixel_values"]])
        torch.jit.save(traced_model, self.checkpoint_path)
        
        return 0


def main():

   
    # sample image url 
    image_url = 'http://images.cocodataset.org/val2017/000000039769.jpg'

    # define pretrained model version
    model_source = 'openai'
    model_version = 'clip-vit-large-patch14'
    model_path = model_source + '/'+model_version

     # checkpoint path 
    checkpoint_path = 'checkpoints/' + model_version + '.pt'
    

    # initial the class 
    SM = SaveModel(model_path,checkpoint_path,image_url)

    # load pretrained model
    model = SM.load_model()

    # save the  model with torchscript format 
    demo = SM.save_model(model)
    
if __name__ == "__main__":
    main()

