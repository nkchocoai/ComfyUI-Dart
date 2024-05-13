import re

from transformers import AutoTokenizer

from ..defs.token import (
    RATING_EOS,
    COPYRIGHT_EOS,
    CHARACTER_EOS,
    GENERAL_EOS,
    PEOPLE_TAGS_LIST,
)


class DartTokenizer:
    def __init__(self, model_name, special_tags):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, trust_remote_code=True
        )
        self.special_tags = special_tags
        self.token_id_table = {
            tag: self.tokenizer.convert_tokens_to_ids(tag) for tag in self.special_tags
        }

    def get_token_id(self, token):
        if token not in self.token_id_table:
            self.token_id_table[token] = self.tokenizer.convert_tokens_to_ids(token)
        return self.token_id_table[token]

    def convert_tokens_to_ids(self, tags_list):
        return self.tokenizer.convert_tokens_to_ids(tags_list)

    def decode(self, token_ids, skip_special_tokens=True):
        return self.tokenizer.decode(token_ids, skip_special_tokens=skip_special_tokens)

    # refer. https://huggingface.co/spaces/p1atdev/danbooru-tags-transformer/blob/main/app.py#L218-L267
    def decode_by_animagine(self, token_ids):
        rearranged_tokens = self.rearrange_by_animagine(token_ids)

        decoded = self.tokenizer.decode(rearranged_tokens, skip_special_tokens=True)

        # fix "nsfw" tag
        decoded = decoded.replace("rating:nsfw", "nsfw")

        return decoded

    def rearrange_by_animagine(self, token_ids):
        (
            rating_part,
            copyright_part,
            character_part,
            people_part,
            other_general_part,
        ) = self.split_parts(token_ids)

        # AnimagineXL v3 style order
        rearranged_tokens = (
            people_part
            + character_part
            + copyright_part
            + other_general_part
            + rating_part
        )
        special_tag_ids = self.convert_tokens_to_ids(self.special_tags)
        rearranged_tokens = [
            token for token in rearranged_tokens if token not in special_tag_ids
        ]

        return rearranged_tokens

    def split_parts(self, token_ids):
        def get_part(eos_token_id, remains_part):
            part = []
            for i, token_id in enumerate(remains_part):
                if token_id == eos_token_id:
                    return part, remains_part[i:]

                part.append(token_id)

            raise Exception("The provided EOS token was not found in the token_ids.")

        # get each part
        rating_part, remains = get_part(self.get_token_id(RATING_EOS), token_ids)
        copyright_part, remains = get_part(self.get_token_id(COPYRIGHT_EOS), remains)
        character_part, remains = get_part(self.get_token_id(CHARACTER_EOS), remains)
        general_part, _ = get_part(self.get_token_id(GENERAL_EOS), remains)

        # separete people tags (1girl, 1boy, no humans...)
        people_part, other_general_part = self.split_people_tokens_part(general_part)

        # remove "rating:sfw"
        sfw_tag_id = self.tokenizer.convert_tokens_to_ids("sfw")
        rating_part = [token for token in rating_part if token != sfw_tag_id]

        return (
            rating_part,
            copyright_part,
            character_part,
            people_part,
            other_general_part,
        )

    def split_people_tokens_part(self, token_ids):
        people_tokens = []
        other_tokens = []

        people_tag_ids_list = self.convert_tokens_to_ids(PEOPLE_TAGS_LIST)
        for token in token_ids:
            if token in people_tag_ids_list:
                people_tokens.append(token)
            else:
                other_tokens.append(token)

        return people_tokens, other_tokens

    def get_ban_tags_from_regex(self, regex_patterns):
        ban_tags = set()
        patterns = [re.compile(regex_pattern) for regex_pattern in regex_patterns]
        for pattern in patterns:
            for tag in self.tokenizer.vocab:
                if pattern.match(tag):
                    ban_tags.add(tag)
        return ban_tags

    def decode_by_splited_parts(self, token_ids):
        decoded_parts = [self.decode(part) for part in self.split_parts(token_ids)]
        return (*decoded_parts,)
