from ..dart.prompt import DartPromptComposer
from ..dart.defs.combo_v2 import RATINGS, ASPECT_RATIOS, LENGTHS, IDENTITIES

from .base import BaseNode


class DanbooruTagsTransformerComposePromptV2(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
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
                "rating": (RATINGS,),
                "aspect_ratio": (
                    ASPECT_RATIOS,
                    {
                        "default": "square",
                    },
                ),
                "length": (
                    LENGTHS,
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
                "identity": (
                    IDENTITIES,
                    {
                        "default": "none",
                    },
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "compose"

    def compose(
        self, copyright, character, rating, aspect_ratio, length, general, identity
    ):
        prompt = DartPromptComposer.compose_v2(
            copyright, character, rating, aspect_ratio, length, general, identity
        )
        return (prompt,)


class DanbooruTagsTransformerGetAspectRatio(BaseNode):
    MAX_RESOLUTION = 16384

    @classmethod
    def INPUT_TYPES(cls):
        input_types = {
            "required": {
                "width": (
                    "INT",
                    {"default": 1024, "min": 16, "max": cls.MAX_RESOLUTION, "step": 8},
                ),
                "height": (
                    "INT",
                    {"default": 1024, "min": 16, "max": cls.MAX_RESOLUTION, "step": 8},
                ),
            },
        }

        return input_types

    RETURN_TYPES = (ASPECT_RATIOS,)
    RETURN_NAMES = ("ASPECT_RATIOS",)
    FUNCTION = "get_aspect_ratio"

    def get_aspect_ratio(self, width, height):
        ratio = width / height
        aspect_ratio = "ultra_wide"
        if 2 / 1 > ratio > 9 / 8:
            aspect_ratio = "wide"
        elif 9 / 8 >= ratio >= 8 / 9:
            aspect_ratio = "wide"
        elif 8 / 9 > ratio > 1 / 2:
            aspect_ratio = "tall"
        elif 1 / 2 >= ratio:
            aspect_ratio = "ultra_tall"
        return (aspect_ratio,)
