from PIL import Image
import numpy as np
from .bitplane import decompose, recombine
from .dna_encoding import encode, decode
from .chaotic_map import generate_logistic_sequence
from .subsequence import apply_ops
from .permutation import permute_positions

def encrypt(image: Image.Image, key: float) -> Image.Image:
    bplanes = decompose(image)
    new_planes = []
    for plane in bplanes:
        dna_seq = encode(plane)
        ks1 = generate_logistic_sequence(key, 3.99, len(dna_seq))
        mod_dna = apply_ops(dna_seq, ks1)
        mod_plane = decode(mod_dna, plane.shape)
        ks2 = generate_logistic_sequence(key + 1, 3.99, plane.size)
        perm_plane = permute_positions(mod_plane, ks2)
        new_planes.append(perm_plane)
    return recombine(new_planes)