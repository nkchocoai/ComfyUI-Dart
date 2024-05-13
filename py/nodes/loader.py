from ..dart.model import DartModel
from ..dart.tokenizer.tokenizer import DartTokenizer
from ..dart.tokenizer.tokenizer_v2 import DartTokenizerV2

from .base import BaseNode
from ..dart.defs.token import SPECIAL_TAGS
from ..dart.defs.token_v2 import SPECIAL_TAGS_V2


class DanbooruTagsTransformerLoader(BaseNode):
    MODEL_NAMES = {
        "dart-v1-sft": {
            "model_name": "p1atdev/dart-v1-sft",
            "special_tags": SPECIAL_TAGS,
            "tokenizer": DartTokenizer,
        },
        "dart-v2-moe-sft": {
            "model_name": "p1atdev/dart-v2-moe-sft",
            "special_tags": SPECIAL_TAGS_V2,
            "tokenizer": DartTokenizerV2,
        },
        "dart-v2-sft": {
            "model_name": "p1atdev/dart-v2-sft",
            "special_tags": SPECIAL_TAGS_V2,
            "tokenizer": DartTokenizerV2,
        },
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
        model_name = self.MODEL_NAMES[model]["model_name"]
        special_tags = self.MODEL_NAMES[model]["special_tags"]
        dart_model = DartModel(model_name)
        tokenizer = self.MODEL_NAMES[model]["tokenizer"](model_name, special_tags)
        return (dart_model, tokenizer)
