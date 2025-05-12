from PIL import Image
import numpy as np

def decompose(image: Image.Image) -> list[np.ndarray]:
    """Decompose a grayscale image into its 8 bit-planes."""
    arr = np.array(image.convert("L"), dtype=np.uint8)
    return [((arr >> i) & 1).astype(np.uint8) for i in range(8)]


def recombine(bitplanes: list[np.ndarray]) -> Image.Image:
    """Recombine 8 bit-planes into a grayscale image."""
    arr = sum((bitplanes[i] << i) for i in range(8)).astype(np.uint8)
    return Image.fromarray(arr)