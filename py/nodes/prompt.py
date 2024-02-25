from ..dart.prompt import DartPromptComposer
from ..dart.defs.combo import RATINGS, LENGTHS

from .base import BaseNode


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
