import os
from PIL import Image
import numpy as np

from settings import SAMPLE_IMAGES_PATH

__all__ = (
    'resize_image',
    'get_sample_images',
)


def resize_image(image_path, desired_size):
    im = Image.open(image_path)
    old_size = im.size

    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)

    new_im = Image.new("RGB", (desired_size, desired_size), color='White')
    new_im.paste(im, ((desired_size - new_size[0]) // 2,
                      (desired_size - new_size[1]) // 2))

    img_array = np.asarray(new_im)
    img_array = img_array.astype('float32')

    return {
        'original': im,
        'sized': img_array
    }


def get_sample_images(category=None):
    """Get sample images.

    :return:
    """
    if category:
        return sorted(
            [
                os.path.join(SAMPLE_IMAGES_PATH, __f)
                for __f
                in os.listdir(SAMPLE_IMAGES_PATH)
                if (
                    os.path.isfile(os.path.join(SAMPLE_IMAGES_PATH, __f))
                    and category in __f
                )
            ]
        )

    return sorted(
        [
            os.path.join(SAMPLE_IMAGES_PATH, __f)
            for __f
            in os.listdir(SAMPLE_IMAGES_PATH)
            if os.path.isfile(os.path.join(SAMPLE_IMAGES_PATH, __f))
        ]
    )
