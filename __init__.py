from .py.nodes.generate import DanbooruTagsTransformerGenerate
from .py.nodes.prompt import DanbooruTagsTransformerComposePrompt
from .py.nodes.config import DanbooruTagsTransformerGenerationConfig
from .py.nodes.advanced.generate import DanbooruTagsTransformerGenerateAdvanced
from .py.nodes.advanced.decode import (
    DanbooruTagsTransformerDecode,
    DanbooruTagsTransformerDecodeBySplitedParts,
)
from .py.nodes.advanced.token_ids import (
    DanbooruTagsTransformerRearrangedByAnimagine,
    DanbooruTagsTransformerRemoveTagToken,
)
from .py.nodes.ban_tags import DanbooruTagsTransformerBanTagsFromRegex

NODE_CLASS_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": DanbooruTagsTransformerGenerate,
    "DanbooruTagsTransformerComposePrompt": DanbooruTagsTransformerComposePrompt,
    "DanbooruTagsTransformerGenerationConfig": DanbooruTagsTransformerGenerationConfig,
    "DanbooruTagsTransformerBanTagsFromRegex": DanbooruTagsTransformerBanTagsFromRegex,
    # Advanced
    "DanbooruTagsTransformerGenerateAdvanced": DanbooruTagsTransformerGenerateAdvanced,
    "DanbooruTagsTransformerDecode": DanbooruTagsTransformerDecode,
    "DanbooruTagsTransformerDecodeBySplitedParts": DanbooruTagsTransformerDecodeBySplitedParts,
    "DanbooruTagsTransformerRearrangedByAnimagine": DanbooruTagsTransformerRearrangedByAnimagine,
    "DanbooruTagsTransformerRemoveTagToken": DanbooruTagsTransformerRemoveTagToken,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": "Dart Generate",
    "DanbooruTagsTransformerComposePrompt": "Dart Compose Prompt",
    "DanbooruTagsTransformerGenerationConfig": "Dart Generation Config",
    "DanbooruTagsTransformerBanTagsFromRegex": "Dart Ban Tags From Regex",
    # Advanced
    "DanbooruTagsTransformerGenerateAdvanced": "Dart Generate(Advanced)",
    "DanbooruTagsTransformerDecode": "Dart Decode",
    "DanbooruTagsTransformerDecodeBySplitedParts": "Dart Decode By Splited Parts",
    "DanbooruTagsTransformerRearrangedByAnimagine": "Dart Rearranged By Animagine",
    "DanbooruTagsTransformerRemoveTagToken": "Dart Remove Tag Token",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
