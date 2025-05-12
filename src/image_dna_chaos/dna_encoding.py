import numpy as np

mapping = {
    '00': 'A', '01': 'C',
    '10': 'G', '11': 'T'
}
inv_mapping = {v: k for k, v in mapping.items()}


def encode(bitplane: np.ndarray) -> list[str]:
    flat = bitplane.flatten()
    seq = [''.join(str(b) for b in flat[i:i+2]) for i in range(0, len(flat), 2)]
    return [mapping[s] for s in seq]


def decode(dna_seq: list[str], shape: tuple) -> np.ndarray:
    bits = ''.join(inv_mapping[n] for n in dna_seq)
    arr = np.frombuffer(bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8)), dtype=np.uint8)
    return arr.reshape(shape)