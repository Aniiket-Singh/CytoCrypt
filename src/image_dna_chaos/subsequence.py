from typing import List

def apply_ops(dna_seq: List[str], keystream: list[float]) -> List[str]:
    """Apply a simple reversible subsequence operation (circular rotation)."""
    if not dna_seq:
        return dna_seq
    k = int(keystream[0] * len(dna_seq))
    return dna_seq[k:] + dna_seq[:k]


def inverse_ops(dna_seq: List[str], keystream: list[float]) -> List[str]:
    """Invert the circular rotation applied in apply_ops."""
    if not dna_seq:
        return dna_seq
    k = int(keystream[0] * len(dna_seq))
    return dna_seq[-k:] + dna_seq[:-k]