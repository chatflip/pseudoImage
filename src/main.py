import argparse
from PseudoImage import PseudoImage


def config():
    

def main() -> None:
    image_path = "image.jpg"
    pseudo_image_maker = PseudoImage(image_scale=30)
    pseudo_image_maker(image_path)


if __name__ == "__main__":
    
    main()
