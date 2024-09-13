import logging

import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

logging.basicConfig(level=logging.INFO)


class ImageCaptioningModel:
    def __init__(self, model_name="multimodalart/Florence-2-large-no-flash-attn"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16
        self.model_name = model_name
        self.model = None
        self.processor = None
        self.load_model()

    def load_model(self):
        try:
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name, torch_dtype=self.torch_dtype, trust_remote_code=True
            ).to(self.device)
            self.processor = AutoProcessor.from_pretrained(
                self.model_name, trust_remote_code=True
            )
            logging.info(f"Model loaded successfully on {self.device}")
        except Exception as e:
            logging.error(f"Error loading model: {e}")

    def generate_caption(self, image_input, concept_sentence=False):
        # Check if the input is a PIL Image object or a path
        if isinstance(image_input, str):
            # If it's a string, assume it's a file path
            try:
                image = Image.open(image_input).convert("RGB")
            except Exception as e:
                logging.error(f"Error opening image: {e}")
                return None
        elif isinstance(image_input, Image.Image):
            # If it's already a PIL Image object, use it directly
            image = image_input
        else:
            raise ValueError(f"Invalid image input: {image_input}")

        return self._generate_caption_from_image(image, concept_sentence)

    def _generate_caption_from_image(self, image, concept_sentence):
        prompt = "<DETAILED_CAPTION>"
        try:
            inputs = self.processor(text=prompt, images=image, return_tensors="pt").to(
                self.device
            )
            inputs["input_ids"] = inputs["input_ids"].to(self.device)
            inputs["pixel_values"] = inputs["pixel_values"].to(
                self.device, self.torch_dtype
            )

            generated_ids = self.model.generate(
                input_ids=inputs["input_ids"],
                pixel_values=inputs["pixel_values"],
                max_new_tokens=1024,
                num_beams=3,
            )

            generated_text = self.processor.batch_decode(
                generated_ids, skip_special_tokens=False
            )[0]

            parsed_answer = self.processor.post_process_generation(
                generated_text, task=prompt, image_size=(image.width, image.height)
            )
            caption_text = parsed_answer["<DETAILED_CAPTION>"].replace(
                "The image shows ", ""
            )
            if concept_sentence:
                caption_text = f"{caption_text} [trigger]"

            return caption_text

        except Exception as e:
            logging.error(f"Error generating caption: {e}")
            return None

    def unload_model(self):
        # Cleanup
        self.model.to("cpu")
        del self.model
        del self.processor
        torch.cuda.empty_cache()
