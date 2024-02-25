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
                "remove_tags": (
                    "STRING",
                    {
                        "default": "",
                        "display": "remove tags",
                        "multiline": True,
                    },
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"

    def generate(
        self,
        prompt,
        seed,
        animagine_order=True,
        setting=None,
        ban_tags="",
        remove_tags="",
    ):
        outputs = DartGenerator.generate(prompt, seed, setting, ban_tags)
        token_ids = outputs[0]

        # remove tags
        remove_tag_token_ids = DartDecoder.tokenizer.encode_plus(remove_tags).input_ids
        token_ids = [token for token in token_ids if token not in remove_tag_token_ids]

        if animagine_order:
            result = DartDecoder.decode_by_animagine(token_ids)
        else:
            result = DartDecoder.decode(token_ids)
        return (result,)
