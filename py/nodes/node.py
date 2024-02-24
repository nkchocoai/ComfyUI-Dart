from ..dart.generator import DartGenerator
from ..dart.prompt import DartPromptComposer
from ..dart.definitions import RATINGS, LENGTHS

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


class DanbooruTagsTransformerComposePrompt(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "rating": (list(RATINGS.keys()),),
                "copyright": (
                    "STRING",
                    {
                        "multiline": False,
                    },
                ),
                "character": (
                    "STRING",
                    {
                        "multiline": False,
                    },
                ),
                "length": (
                    list(LENGTHS.keys()),
                    {
                        "default": "long",
                    },
                ),
                "general": (
                    "STRING",
                    {
                        "default": "1girl",
                        "multiline": True,
                    },
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "compose"

    def compose(self, rating, copyright, character, length, general):
        prompt = DartPromptComposer.compose(
            rating, copyright, character, length, general
        )
        return (prompt,)
