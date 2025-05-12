import numpy as np
from PIL import Image
from image_dna_chaos.bitplane import decompose, recombine
import os


def test_decompose_recombine_sample_image():

    # Path to the sample image in the repo
    sample_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'samples', 'mandrill.png')
    img = Image.open(sample_path).convert("L")

    # Decompose and recombine
    bitplanes = decompose(img)
    reconstructed = recombine(bitplanes)
    rec_arr = np.array(reconstructed)
    orig_arr = np.array(img)

    # Assert pixel-perfect equality
    assert np.array_equal(orig_arr, rec_arr), "Recombined image does not match original"