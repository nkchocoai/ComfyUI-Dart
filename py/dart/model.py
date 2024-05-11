import numpy as np
import torch
from transformers import AutoModelForCausalLM

from ..dart.tokenizer import DartTokenizer


class DartModel:
    def __init__(self, model_name):
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, torch_dtype=torch.bfloat16
        )

    def generate(
        self, tokenizer: DartTokenizer, prompt, seed, config=None, ban_tags=""
    ):
        self.set_seed(seed)

        inputs = tokenizer.tokenizer(prompt, return_tensors="pt").input_ids
        bad_words_ids = tokenizer.tokenizer.encode_plus(ban_tags).input_ids
        if len(bad_words_ids) == 0:
            bad_words_ids = None
        else:
            bad_words_ids = [[token] for token in bad_words_ids]

        with torch.no_grad():
            generation_config = self.model.generation_config
            if config is not None:
                generation_config = self.update_generation_config(
                    generation_config, config
                )
            outputs = self.model.generate(
                inputs, generation_config=generation_config, bad_words_ids=bad_words_ids
            )

        return outputs

    # refer. https://github.com/huggingface/transformers/blob/6b1ff250842f52136d5159bb67a26b50ba01485d/examples/run_generation.py#L74
    @classmethod
    def set_seed(cls, seed):
        n_gpu = torch.cuda.device_count()
        np.random.seed(seed)
        torch.manual_seed(seed)
        if n_gpu > 0:
            torch.cuda.manual_seed_all(seed)

    @classmethod
    def update_generation_config(cls, generation_config, config):
        # https://huggingface.co/docs/transformers/ja/main_classes/text_generation#transformers.GenerationConfig
        generation_config.max_new_tokens = config["max_new_tokens"]
        generation_config.min_new_tokens = config["min_new_tokens"]
        generation_config.temperature = config["temperature"]
        generation_config.top_p = config["top_p"]
        generation_config.top_k = config["top_k"]
        generation_config.num_beams = config["num_beams"]
        return generation_config
