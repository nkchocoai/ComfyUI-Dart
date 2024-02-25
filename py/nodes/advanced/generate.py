from ...dart.generator import DartGenerator

from ..base import BaseNode


class DanbooruTagsTransformerGenerateAdvanced(BaseNode):
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

    RETURN_TYPES = ("DART_TOKEN_IDS",)
    FUNCTION = "generate"

    def generate(self, prompt, seed, setting=None, ban_tags=""):
        outputs = DartGenerator.generate(prompt, seed, setting, ban_tags)
        token_ids = outputs[0]
        return (token_ids,)
