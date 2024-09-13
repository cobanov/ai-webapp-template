import argparse
import logging
import os

from model import ImageCaptioningModel

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="Image Captioning App")
    parser.add_argument("images", nargs="+", help="Paths to image files")
    parser.add_argument(
        "--concept_sentence", action="store_true", help="Append [trigger] to captions"
    )

    args = parser.parse_args()

    model = ImageCaptioningModel()

    for image_path in args.images:
        if not os.path.exists(image_path):
            logging.error(f"Image path does not exist: {image_path}")
            continue

        try:
            caption = model.generate_caption(image_path, args.concept_sentence)
            print(f"Caption for {image_path}:")
            print(caption)
            print("")
        except Exception as e:
            logging.error(f"Error generating caption for {image_path}: {e}")

    model.unload_model()


if __name__ == "__main__":
    main()
