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
    FUNCTION = "process"
    CATEGORY = "CEM"

    def process(self, images, reverse):
        print(images)
        return torch.cat(list(images).reverse() if reverse else list(images), dim=0)

NODE_CLASS_MAPPINGS = {
    "ProcessImageBatch": ProcessImageBatch
}
