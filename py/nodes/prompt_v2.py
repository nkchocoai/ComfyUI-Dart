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
