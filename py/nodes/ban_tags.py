from ..dart.tokenizer import DartTokenizer

from .base import BaseNode


class DanbooruTagsTransformerBanTagsFromRegex(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "tokenizer": ("DART_TOKENIZER",),
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

    def compose(self, tokenizer: DartTokenizer, patterns):
        ban_tags = tokenizer.get_ban_tags_from_regex(patterns.splitlines())
        return (", ".join(ban_tags),)
