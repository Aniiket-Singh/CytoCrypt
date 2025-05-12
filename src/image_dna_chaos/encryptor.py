from PIL import Image
import numpy as np
from .bitplane import decompose, recombine
from .dna_encoding import encode, decode
from .chaotic_map import generate_logistic_sequence
from .subsequence import apply_ops
from .permutation import permute_positions


def encrypt(image: Image.Image, key: float) -> Image.Image:
    # 1. Decompose into bit-planes
    bplanes = decompose(image)

    # Placeholder for new bit-planes post DNA ops and permutation
    new_planes = []

    # For each bit-plane:
    for plane in bplanes:
        # 2. Encode to DNA sequence
        dna_seq = encode(plane)

        # 3. Generate keystream for this DNA sequence
        ks1 = generate_logistic_sequence(key, 3.99, len(dna_seq))
        # 4. Apply subsequence operations
        mod_dna = apply_ops(dna_seq, ks1)

        # 5. Decode back to bit-plane
        mod_plane = decode(mod_dna, plane.shape)

        # 6. Permute pixel positions
        ks2 = generate_logistic_sequence(key + 1, 3.99, plane.size)
        perm_plane = permute_positions(mod_plane, ks2)

        new_planes.append(perm_plane)

    # 7. Recombine into encrypted image
    cipher = recombine(new_planes)
    return cipher