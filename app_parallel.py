import argparse
import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from model import ImageCaptioningModel

logging.basicConfig(level=logging.INFO)


def generate_caption_for_image(image_path, model, concept_sentence):
    if not os.path.exists(image_path):
        logging.error(f"Image path does not exist: {image_path}")
        return None, image_path

    try:
        caption = model.generate_caption(image_path, concept_sentence)
        return caption, image_path
    except Exception as e:
        logging.error(f"Error generating caption for {image_path}: {e}")
        return None, image_path


def main():
    parser = argparse.ArgumentParser(description="Image Captioning App")
    parser.add_argument("images", nargs="+", help="Paths to image files")
    parser.add_argument(
        "--concept_sentence", action="store_true", help="Append [trigger] to captions"
    )
    parser.add_argument(
        "--workers", type=int, default=4, help="Number of parallel workers"
    )

    args = parser.parse_args()

    model = ImageCaptioningModel()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [
            executor.submit(
                generate_caption_for_image, img, model, args.concept_sentence
            )
            for img in args.images
        ]

        for future in as_completed(futures):
            caption, image_path = future.result()
            if caption:
                print(f"Caption for {image_path}:")
                print(caption)
                print("")

    model.unload_model()


if __name__ == "__main__":
    main()
