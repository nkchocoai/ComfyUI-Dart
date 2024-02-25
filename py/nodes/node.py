from ..dart.generator import DartGenerator
from ..dart.prompt import DartPromptComposer
from ..dart.defs.combo import RATINGS, LENGTHS

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

    def generate(self, prompt, seed, setting=None, ban_tags=""):
        outputs = DartGenerator.generate(prompt, seed, setting, ban_tags)
        result = DartGenerator.decode(outputs)
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


class DanbooruTagsTransformerGenerationConfig(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "max_new_tokens": (
                    "INT",
                    {"default": 128, "min": 1, "max": 256, "step": 1},
                ),
                "min_new_tokens": (
                    "INT",
                    {"default": 0, "min": 0, "max": 255, "step": 1},
                ),
                "temperature": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.1},
                ),
                "top_p": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.1},
                ),
                "top_k": (
                    "INT",
                    {"default": 100, "min": 1, "max": 500, "step": 1},
                ),
                "num_beams": (
                    "INT",
                    {"default": 1, "min": 1, "max": 10, "step": 1},
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("DART SETTING",)
    FUNCTION = "compose"

    def compose(self, **kwargs):
        print(kwargs)
        return (kwargs,)
