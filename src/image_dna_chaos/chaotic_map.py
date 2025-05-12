def generate_logistic_sequence(x0: float, r: float, length: int) -> list[float]:
    """Generate a logistic map keystream."""
    seq = []
    x = x0
    for _ in range(length):
        x = r * x * (1 - x)
        seq.append(x)
    return seq