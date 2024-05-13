import re

from transformers import AutoTokenizer

from ..defs.token_v2 import (
    RATING_SFW,
    RATING_GENERAL,
    RATING_SENSITIVE,
    RATING_NSFW,
    RATING_QUESTIONABLE,
    RATING_EXPLICIT,
)

from ..defs.token import (
    PEOPLE_TAGS_LIST,
)


class DartTokenizerV2:
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
        tokens = [
            self.tokenizer.decode([token_id], skip_special_tokens=skip_special_tokens)
            for token_id in token_ids
        ]
        return ", ".join([token for token in tokens if token])

    def decode_by_animagine(self, token_ids):
        rearranged_tokens = self.rearrange_by_animagine(token_ids)

        tokens = [
            self.tokenizer.decode([token_id], skip_special_tokens=True)
            for token_id in rearranged_tokens
        ]

        return ", ".join([token for token in tokens if token])

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
        sections = []
        section = []
        special_tokens = [
            self.tokenizer.convert_tokens_to_ids(tag) for tag in self.special_tags
        ]
        for token_id in token_ids:
            if token_id in special_tokens:
                if len(section) > 0:
                    sections.append(section)
                section = []
            else:
                section.append(token_id)
        copyright_part = sections[0]
        character_part = sections[1]
        rating_part = [
            token_id
            for token_id in token_ids
            if token_id
            in [
                self.tokenizer.convert_tokens_to_ids(tag)
                for tag in [
                    RATING_SFW,
                    RATING_GENERAL,
                    RATING_SENSITIVE,
                    RATING_NSFW,
                    RATING_QUESTIONABLE,
                    RATING_EXPLICIT,
                ]
            ]
        ]
        general_part = sections[2] + sections[3]

        # separete people tags (1girl, 1boy, no humans...)
        people_part, other_general_part = self.split_people_tokens_part(general_part)

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
        decoded_parts = [
            self.decode(part, skip_special_tokens=False)
            for part in self.split_parts(token_ids)
        ]
        decoded_parts[0] = decoded_parts[0].replace("<|", "").replace("|>", "")
        return (*decoded_parts,)
