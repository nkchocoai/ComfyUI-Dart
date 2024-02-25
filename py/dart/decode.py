from .defs.token import (
    RATING_EOS,
    COPYRIGHT_EOS,
    CHARACTER_EOS,
    GENERAL_EOS,
    SPECIAL_TAGS,
    PEOPLE_TAGS_LIST,
)


class DartDecoder:
    @classmethod
    def init(cls, tokenizer):
        cls.tokenizer = tokenizer
        cls.token_id_table = {
            tag: cls.tokenizer.convert_tokens_to_ids(tag) for tag in SPECIAL_TAGS
        }

    @classmethod
    def get_token_id(cls, token):
        if token not in cls.token_id_table:
            cls.token_id_table[token] = cls.tokenizer.convert_tokens_to_ids(token)
        return cls.token_id_table[token]

    @classmethod
    def convert_tokens_to_ids(cls, tags_list):
        return cls.tokenizer.convert_tokens_to_ids(tags_list)

    @classmethod
    def decode(cls, token_ids, skip_special_tokens=True):
        return cls.tokenizer.decode(token_ids, skip_special_tokens=skip_special_tokens)

    # refer. https://huggingface.co/spaces/p1atdev/danbooru-tags-transformer/blob/main/app.py#L218-L267
    @classmethod
    def decode_by_animagine(cls, token_ids):
        rearranged_tokens = cls.rearrange_by_animagine(token_ids)

        decoded = cls.tokenizer.decode(rearranged_tokens, skip_special_tokens=True)

        # fix "nsfw" tag
        decoded = decoded.replace("rating:nsfw", "nsfw")

        return decoded

    @classmethod
    def rearrange_by_animagine(cls, token_ids):
        (
            rating_part,
            copyright_part,
            character_part,
            people_part,
            other_general_part,
        ) = cls.split_parts(token_ids)

        # AnimagineXL v3 style order
        rearranged_tokens = (
            people_part
            + character_part
            + copyright_part
            + other_general_part
            + rating_part
        )
        special_tag_ids = cls.convert_tokens_to_ids(SPECIAL_TAGS)
        rearranged_tokens = [
            token for token in rearranged_tokens if token not in special_tag_ids
        ]

        return rearranged_tokens

    @classmethod
    def split_parts(cls, token_ids):
        def get_part(eos_token_id, remains_part):
            part = []
            for i, token_id in enumerate(remains_part):
                if token_id == eos_token_id:
                    return part, remains_part[i:]

                part.append(token_id)

            raise Exception("The provided EOS token was not found in the token_ids.")

        # get each part
        rating_part, remains = get_part(cls.get_token_id(RATING_EOS), token_ids)
        copyright_part, remains = get_part(cls.get_token_id(COPYRIGHT_EOS), remains)
        character_part, remains = get_part(cls.get_token_id(CHARACTER_EOS), remains)
        general_part, _ = get_part(cls.get_token_id(GENERAL_EOS), remains)

        # separete people tags (1girl, 1boy, no humans...)
        people_part, other_general_part = cls.split_people_tokens_part(general_part)

        # remove "rating:sfw"
        sfw_tag_id = cls.tokenizer.convert_tokens_to_ids("sfw")
        rating_part = [token for token in rating_part if token != sfw_tag_id]

        return (
            rating_part,
            copyright_part,
            character_part,
            people_part,
            other_general_part,
        )

    @classmethod
    def split_people_tokens_part(cls, token_ids):
        people_tokens = []
        other_tokens = []

        people_tag_ids_list = cls.convert_tokens_to_ids(PEOPLE_TAGS_LIST)
        for token in token_ids:
            if token in people_tag_ids_list:
                people_tokens.append(token)
            else:
                other_tokens.append(token)

        return people_tokens, other_tokens
