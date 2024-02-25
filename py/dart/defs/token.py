import os

# refer. https://huggingface.co/spaces/p1atdev/danbooru-tags-transformer/blob/main/app.py#L63-L119
BOS = "<|bos|>"
EOS = "<|eos|>"
RATING_BOS = "<rating>"
RATING_EOS = "</rating>"
COPYRIGHT_BOS = "<copyright>"
COPYRIGHT_EOS = "</copyright>"
CHARACTER_BOS = "<character>"
CHARACTER_EOS = "</character>"
GENERAL_BOS = "<general>"
GENERAL_EOS = "</general>"

INPUT_END = "<|input_end|>"

LENGTH_VERY_SHORT = "<|very_short|>"
LENGTH_SHORT = "<|short|>"
LENGTH_LONG = "<|long|>"
LENGTH_VERY_LONG = "<|very_long|>"

SPECIAL_TAGS = [
    BOS,
    EOS,
    RATING_BOS,
    RATING_EOS,
    COPYRIGHT_BOS,
    COPYRIGHT_EOS,
    CHARACTER_BOS,
    CHARACTER_EOS,
    GENERAL_BOS,
    GENERAL_EOS,
    INPUT_END,
    LENGTH_VERY_SHORT,
    LENGTH_SHORT,
    LENGTH_LONG,
    LENGTH_VERY_LONG,
]


def load_tags(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip() != ""]

    return lines


assets_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "assets")
print(assets_dir)
PEOPLE_TAGS_LIST = load_tags(os.path.join(assets_dir, "people.txt"))
