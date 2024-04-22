"""Practice with Recursion."""


def f(n: int, k: int) -> int:
    """N*k defined recursively."""
    if n == 0:
        return n
    else:
        return f(n - 1, k) + k
