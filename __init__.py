from .py.nodes.generate import DanbooruTagsTransformerGenerate
from .py.nodes.prompt import DanbooruTagsTransformerComposePrompt
from .py.nodes.config import DanbooruTagsTransformerGenerationConfig
from .py.nodes.advanced.generate import DanbooruTagsTransformerGenerateAdvanced
from .py.nodes.advanced.decode import (
    DanbooruTagsTransformerDecode,
    DanbooruTagsTransformerDecodeBySplitedParts,
)
from .py.nodes.advanced.token_ids import DanbooruTagsTransformerRearrangedByAnimagine

NODE_CLASS_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": DanbooruTagsTransformerGenerate,
    "DanbooruTagsTransformerComposePrompt": DanbooruTagsTransformerComposePrompt,
    "DanbooruTagsTransformerGenerationConfig": DanbooruTagsTransformerGenerationConfig,
    # Advanced
    "DanbooruTagsTransformerGenerateAdvanced": DanbooruTagsTransformerGenerateAdvanced,
    "DanbooruTagsTransformerDecode": DanbooruTagsTransformerDecode,
    "DanbooruTagsTransformerRearrangedByAnimagine": DanbooruTagsTransformerRearrangedByAnimagine,
    "DanbooruTagsTransformerDecodeBySplitedParts": DanbooruTagsTransformerDecodeBySplitedParts,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": "Dart Generate",
    "DanbooruTagsTransformerComposePrompt": "Dart Compose Prompt",
    "DanbooruTagsTransformerGenerationConfig": "Dart Generation Config",
    # Advanced
    "DanbooruTagsTransformerGenerateAdvanced": "Dart Generate(Advanced)",
    "DanbooruTagsTransformerDecode": "Dart Decode",
    "DanbooruTagsTransformerRearrangedByAnimagine": "Dart Rearranged By Animagine",
    "DanbooruTagsTransformerDecodeBySplitedParts": "Dart Decode By Splited Parts",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
