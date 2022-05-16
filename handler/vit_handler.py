'''
Module for image classification default handler
''' #
import torch
import torch.nn.functional as F
from torchvision import transforms

from ts.torch_handler.vision_handler import VisionHandler



class ImageEmbeddingHandler(VisionHandler):
    """
    ImageEmbedding handler class. This handler takes an image
    and returns the embedded vector of that image.
    """

    # These are the standard Imagenet dimensions
    # and statistics
    IMAGE_SIZE = 224
    MEAN = torch.tensor([0.48145466, 0.4578275, 0.40821073])
    STD = torch.tensor([0.26862954, 0.26130258, 0.27577711])

    image_processing = transforms.Compose([
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=MEAN, std=STD)
    ])

    def postprocess(self, data):
        return data