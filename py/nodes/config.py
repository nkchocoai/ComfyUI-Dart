from .base import BaseNode


class DanbooruTagsTransformerGenerationConfig(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "max_new_tokens": (
                    "INT",
                    {"default": 128, "min": 1, "max": 256, "step": 1},
                ),
                "min_new_tokens": (
                    "INT",
                    {"default": 0, "min": 0, "max": 255, "step": 1},
                ),
                "temperature": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.1},
                ),
                "top_p": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.1},
                ),
                "top_k": (
                    "INT",
                    {"default": 100, "min": 1, "max": 500, "step": 1},
                ),
                "num_beams": (
                    "INT",
                    {"default": 1, "min": 1, "max": 10, "step": 1},
                ),
            },
        }

        return input_types

    RETURN_TYPES = ("DART SETTING",)
    FUNCTION = "compose"

    def compose(self, **kwargs):
        return (kwargs,)
