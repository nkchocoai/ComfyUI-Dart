from .definitions import RATINGS, LENGTHS


class DartPromptComposer:
    @classmethod
    def compose(cls, rating, copyright, character, length, general):
        prompt = "<|bos|>"
        prompt += f"<rating>{RATINGS[rating]}</rating>"
        prompt += f"<copyright>{copyright}</copyright>"
        prompt += f"<character>{character}</character>"
        prompt += f"<general>{LENGTHS[length]}{general}<|input_end|>"
        return prompt
