from PIL import Image
import numpy as np
from .bitplane import decompose, recombine
from .dna_encoding import encode, decode
from .chaotic_map import generate_logistic_sequence
from .subsequence import inverse_ops
from .permutation import inverse_permute

def decrypt(image: Image.Image, key: float) -> Image.Image:
    bplanes = decompose(image)
    restored = []
    for plane in bplanes:
        ks2 = generate_logistic_sequence(key + 1, 3.99, plane.size)
        inv_plane = inverse_permute(plane, ks2)
        dna_seq = encode(inv_plane)
        ks1 = generate_logistic_sequence(key, 3.99, len(dna_seq))
        orig_dna = inverse_ops(dna_seq, ks1)
        orig_plane = decode(orig_dna, plane.shape)
        restored.append(orig_plane)
    return recombine(restored)