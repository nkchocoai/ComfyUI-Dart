from .py.nodes.loader import DanbooruTagsTransformerLoader
from .py.nodes.generate import DanbooruTagsTransformerGenerate
from .py.nodes.prompt import DanbooruTagsTransformerComposePrompt
from .py.nodes.prompt_v2 import DanbooruTagsTransformerComposePromptV2
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
    "DanbooruTagsTransformerLoader": DanbooruTagsTransformerLoader,
    "DanbooruTagsTransformerGenerate": DanbooruTagsTransformerGenerate,
    "DanbooruTagsTransformerComposePrompt": DanbooruTagsTransformerComposePrompt,
    "DanbooruTagsTransformerComposePromptV2": DanbooruTagsTransformerComposePromptV2,
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
    "DanbooruTagsTransformerLoader": "Dart Load",
    "DanbooruTagsTransformerGenerate": "Dart Generate",
    "DanbooruTagsTransformerComposePrompt": "Dart Compose Prompt",
    "DanbooruTagsTransformerComposePromptV2": "Dart Compose Prompt V2",
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
