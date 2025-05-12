from typing import List


def apply_ops(dna_seq: List[str], keystream: list[float]) -> List[str]:
    """
    Apply a simple reversible subsequence operation (circular rotation)
    based on the first value of keystream.
    """
    seq = dna_seq.copy()
    if not seq:
        return seq
    # Determine rotation amount from keystream[0]
    k = int(keystream[0] * len(seq))
    # Circular left rotation
    return seq[k:] + seq[:k]


def inverse_ops(dna_seq: List[str], keystream: list[float]) -> List[str]:
    """
    Invert the circular rotation applied in apply_ops.
    """
    seq = dna_seq.copy()
    if not seq:
        return seq
    k = int(keystream[0] * len(seq))
    # Circular right rotation
    return seq[-k:] + seq[:-k]