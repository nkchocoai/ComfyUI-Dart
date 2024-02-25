from ...dart.decode import DartDecoder

from ..base import BaseNode


class DanbooruTagsTransformerDecode(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "token_ids": ("DART_TOKEN_IDS",),
                "skip_special_tokens": (
                    "BOOLEAN",
                    {
                        "default": True,
                        "display": "skip special tokens",
                    },
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "decode"

    def decode(self, token_ids, skip_special_tokens=True):
        result = DartDecoder.decode(token_ids, skip_special_tokens)
        return (result,)


class DanbooruTagsTransformerDecodeBySplitedParts(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "token_ids": ("DART_TOKEN_IDS",),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("rating", "copyright", "character", "people", "other general")
    FUNCTION = "decode_by_splited_parts"

    def decode_by_splited_parts(self, token_ids):
        decoded_parts = [
            DartDecoder.decode(part) for part in DartDecoder.split_parts(token_ids)
        ]
        return (*decoded_parts,)
