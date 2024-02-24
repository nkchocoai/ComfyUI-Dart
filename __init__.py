from .py.nodes.node import DanbooruTagsTransformerGenerate

NODE_CLASS_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": DanbooruTagsTransformerGenerate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DanbooruTagsTransformerGenerate": "Dart Generate",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
