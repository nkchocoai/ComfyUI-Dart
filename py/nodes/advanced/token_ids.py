from ...dart.decode import DartDecoder

from ..base import BaseNode


class DanbooruTagsTransformerRearrangedByAnimagine(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "token_ids": ("DART_TOKEN_IDS",),
            },
        }

        return input_types

    RETURN_TYPES = ("DART_TOKEN_IDS",)
    FUNCTION = "rearrange"

    def rearrange(self, token_ids):
        rearranged_tokens = DartDecoder.rearrange_by_animagine(token_ids)
        return (rearranged_tokens,)
