from ...dart.model import DartModel
from ...dart.tokenizer.tokenizer import DartTokenizer

from ..base import BaseNode


class DanbooruTagsTransformerGenerateAdvanced(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "model": ("DART_MODEL",),
                "tokenizer": ("DART_TOKENIZER",),
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

    def generate(
        self,
        model: DartModel,
        tokenizer: DartTokenizer,
        prompt,
        seed,
        setting=None,
        ban_tags="",
    ):
        outputs = model.generate(tokenizer, prompt, seed, setting, ban_tags)
        token_ids = outputs[0]
        return (token_ids,)
