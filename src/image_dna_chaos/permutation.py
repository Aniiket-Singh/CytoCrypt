import numpy as np

def permute_positions(arr: np.ndarray, keystream: list[float]) -> np.ndarray:
    """Permute pixel positions of a 2D array based on keystream."""
    flat = arr.flatten()
    # Use keystream slice matching length
    ks = keystream[:flat.size]
    idx = np.argsort(ks)
    return flat[idx].reshape(arr.shape)


def inverse_permute(arr: np.ndarray, keystream: list[float]) -> np.ndarray:
    """Inverse permutation of pixel positions."""
    flat = arr.flatten()
    ks = keystream[:flat.size]
    idx = np.argsort(ks)
    inv = np.empty_like(flat)
    inv[idx] = flat
    return inv.reshape(arr.shape)