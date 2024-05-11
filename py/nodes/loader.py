from ..dart.model import DartModel
from ..dart.tokenizer import DartTokenizer

from .base import BaseNode


class DanbooruTagsTransformerLoader(BaseNode):
    MODEL_NAMES = {
        "dart-v1-sft": "p1atdev/dart-v1-sft",
        "dart-v2-moe-sft": "p1atdev/dart-v2-moe-sft",
        "dart-v2-sft": "p1atdev/dart-v2-sft",
    }

    @classmethod
    def INPUT_TYPES(cls):
        input_types = {
            "required": {
                "model": (list(cls.MODEL_NAMES.keys()),),
            },
        }

        return input_types

    RETURN_TYPES = ("DART_MODEL", "DART_TOKENIZER")
    FUNCTION = "load"

    def load(self, model):
        model_name = self.MODEL_NAMES[model]
        model = DartModel(model_name)
        tokenizer = DartTokenizer(model_name)
        return (model, tokenizer)
