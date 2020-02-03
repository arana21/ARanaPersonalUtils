"""Image IO functions

Use this file to read and write images from/to disk
"""

import os

import cv2
import numpy as np

from src.utils.file_io import BasicFileOps


class ImageIO(BasicFileOps):
    """
    Image IO operations.
    """

    def __init__(self):
        super().__init__()

    def read_image_from_disk(self, file_path):
        """Reads image from disk.

        Args:
            file_path (str): read image from this file

        Returns:
            (np.array)
        """
        self._read_image_from_disk(file_path)
        self._check_file_existance(file_path)

        return cv2.imread(file_path)

    def write_image_to_disk(self, img, file_path):
        """Writes image to disk.

        Args:
            img (np.array): image to be written to file
            file_path (str): file to write the image

        Returns:
            None
        """
        assert type(img, np.array)
        assert type(file_path, str)

        return cv2.imwrite(file_path, img)


class ImageOps(ImageIO):
    """
    Image manipulation operations
    """

    def __init__(self):
        super().__init__()

    def resize_image(self, image, new_shape):
        pass

    def rotate_image(self, image, rot_angle=0):
        pass
