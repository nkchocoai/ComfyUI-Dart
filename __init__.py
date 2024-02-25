from .py.nodes.generate import DanbooruTagsTransformerGenerate
from .py.nodes.prompt import DanbooruTagsTransformerComposePrompt
from .py.nodes.config import DanbooruTagsTransformerGenerationConfig

NODE_CLASS_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": DanbooruTagsTransformerGenerate,
    "DanbooruTagsTransformerComposePrompt": DanbooruTagsTransformerComposePrompt,
    "DanbooruTagsTransformerGenerationConfig": DanbooruTagsTransformerGenerationConfig,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": "Dart Generate",
    "DanbooruTagsTransformerComposePrompt": "Dart Compose Prompt",
    "DanbooruTagsTransformerGenerationConfig": "Dart Generation Config",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
