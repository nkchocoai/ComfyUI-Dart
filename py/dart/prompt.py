from .defs.combo import RATINGS, LENGTHS


class DartPromptComposer:
    @classmethod
    def compose(cls, rating, copyright, character, length, general):
        prompt = "<|bos|>"
        prompt += f"<rating>{RATINGS[rating]}</rating>"
        prompt += f"<copyright>{copyright}</copyright>"
        prompt += f"<character>{character}</character>"
        prompt += f"<general>{LENGTHS[length]}{general}<|input_end|>"
        return prompt

    @classmethod
    def compose_v2(
        cls, copyright, character, rating, aspect_ratio, length, general, identity
    ):
        prompt = (
            f"<|bos|>"
            f"<copyright>{copyright}</copyright>"
            f"<character>{character}</character>"
            f"<|rating:{rating}|><|aspect_ratio:{aspect_ratio}|><|length:{length}|>"
            f"<general>{general}<|identity:{identity}|><|input_end|>"
        )
        return prompt
