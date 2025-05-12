from PIL import Image
import numpy as np
from .bitplane import decompose, recombine
from .dna_encoding import encode, decode
from .chaotic_map import generate_logistic_sequence
from .subsequence import inverse_ops
from .permutation import inverse_permute


def decrypt(image: Image.Image, key: float) -> Image.Image:
    # 1. Decompose into bit-planes
    bplanes = decompose(image)

    restored_planes = []

    for plane in bplanes:
        # 2. Inverse permute pixel positions
        ks2 = generate_logistic_sequence(key + 1, 3.99, plane.size)
        inv_plane = inverse_permute(plane, ks2)

        # 3. Encode to DNA sequence for inverse ops
        dna_seq = encode(inv_plane)

        # 4. Inverse subsequence operations
        ks1 = generate_logistic_sequence(key, 3.99, len(dna_seq))
        orig_dna = inverse_ops(dna_seq, ks1)

        # 5. Decode DNA back to bit-plane
        orig_plane = decode(orig_dna, plane.shape)

        restored_planes.append(orig_plane)

    # 6. Recombine into decrypted image
    plain = recombine(restored_planes)
    return plain