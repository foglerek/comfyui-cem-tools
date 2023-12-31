from torch import Tensor
import torch

MAX_RESOLUTION=8192

class ProcessImageBatch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "reverse": ("BOOLEAN", {"default": False }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "process"
    CATEGORY = "CEM"

    def process(self, images: Tensor, reverse):
        images = torch.flip(images, (0,)) if reverse else images
        return (images,)

NODE_CLASS_MAPPINGS = {
    "ProcessImageBatch": ProcessImageBatch
}
