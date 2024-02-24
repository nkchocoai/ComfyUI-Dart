import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class DartGenerator:
    MODEL_NAME = "p1atdev/dart-v1-sft"

    tokenizer = None
    model = None

    @classmethod
    def load_if_none(cls):
        if cls.tokenizer is None:
            cls.tokenizer = AutoTokenizer.from_pretrained(
                cls.MODEL_NAME, trust_remote_code=True
            )

        if cls.model is None:
            cls.model = AutoModelForCausalLM.from_pretrained(
                cls.MODEL_NAME, torch_dtype=torch.bfloat16
            )

    @classmethod
    def generate(cls, prompt, seed):
        cls.load_if_none()

        cls.set_seed(seed)

        inputs = cls.tokenizer(prompt, return_tensors="pt").input_ids
        with torch.no_grad():
            generation_config = cls.model.generation_config
            outputs = cls.model.generate(inputs, generation_config=generation_config)
            decoded_output = cls.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return decoded_output

    # refer. https://github.com/huggingface/transformers/blob/6b1ff250842f52136d5159bb67a26b50ba01485d/examples/run_generation.py#L74
    @classmethod
    def set_seed(cls, seed):
        n_gpu = torch.cuda.device_count()
        np.random.seed(seed)
        torch.manual_seed(seed)
        if n_gpu > 0:
            torch.cuda.manual_seed_all(seed)
