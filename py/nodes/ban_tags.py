from ..dart.generator import DartGenerator

from .base import BaseNode


class DanbooruTagsTransformerBanTagsFromRegex(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "patterns": (
                    "STRING",
                    {
                        "default": ".+ hair",
                        "multiline": True,
                    },
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "compose"

    def compose(self, patterns):
        ban_tags = DartGenerator.get_ban_tags_from_regex(patterns.splitlines())
        return (", ".join(ban_tags),)
