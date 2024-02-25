from ..dart.generator import DartGenerator
from ..dart.decode import DartDecoder

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
                "animagine_order": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "display": "animagine order",
                    },
                ),
            },
            "optional": {
                "setting": ("DART SETTING",),
                "ban_tags": (
                    "STRING",
                    {
                        "default": "",
                        "display": "ban tags",
                        "multiline": True,
                    },
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"

    def generate(self, prompt, seed, animagine_order=True, setting=None, ban_tags=""):
        outputs = DartGenerator.generate(prompt, seed, setting, ban_tags)
        print(outputs)
        if animagine_order:
            result = DartDecoder.decode_by_animagine(outputs)
        else:
            result = DartDecoder.decode(outputs)
        return (result,)
