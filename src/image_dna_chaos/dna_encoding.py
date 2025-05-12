import numpy as np

mapping = {
    '00': 'A', '01': 'C',
    '10': 'G', '11': 'T'
}
inv_mapping = {v: k for k, v in mapping.items()}

def encode(bitplane: np.ndarray) -> list[str]:
    flat = bitplane.flatten()
    seq = [''.join(str(b) for b in flat[i:i+2]) for i in range(0, len(flat), 2)]
    return [mapping[p] for p in seq]


def decode(dna_seq: list[str], shape: tuple) -> np.ndarray:
    bits = ''.join(inv_mapping[n] for n in dna_seq)
    flat = np.array([int(char) for char in bits], dtype=np.uint8)
    return flat.reshape(shape)