from ..dart.generator import DartGenerator


from .base import BaseNode


class DanbooruTagsTransformerGenerate(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "prompt": (
                    "STRING",
                    {
                        "default": "<|bos|><rating>rating:sfw, rating:general</rating><copyright>original</copyright><character></character><general><|long|>1girl<|input_end|>",
                        "display": "prompt",
                        "multiline": True,
                    },
                ),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2**32 - 1}),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"

    def generate(self, prompt, seed):
        result = DartGenerator.generate(prompt, seed)
        return (result,)
