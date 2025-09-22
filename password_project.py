# secure_password.py
# Usage:
#   from secure_password import generate_password
#   print(generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True))

import secrets
import string

def generate_password(length: int = 16,
                      use_lower: bool = True,
                      use_upper: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = True,
                      avoid_ambiguous: bool = True) -> str:
    """
    Generate a cryptographically secure random password.
    """
    if length < 1:
        raise ValueError("length must be >= 1")

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|~"

    # Optionally remove ambiguous characters like: O,0,I,l,| etc.
    if avoid_ambiguous:
        ambiguous = "O0Il|`'\" ,;:.?!"
        lower = "".join(ch for ch in lower if ch not in ambiguous)
        upper = "".join(ch for ch in upper if ch not in ambiguous)
        digits = "".join(ch for ch in digits if ch not in ambiguous)
        symbols = "".join(ch for ch in symbols if ch not in ambiguous)

    pools = []
    if use_lower and lower: pools.append(lower)
    if use_upper and upper: pools.append(upper)
    if use_digits and digits: pools.append(digits)
    if use_symbols and symbols: pools.append(symbols)

    if not pools:
        raise ValueError("At least one character type must be enabled")

    # Ensure password contains at least one char from each enabled pool
    password_chars = [secrets.choice(pool) for pool in pools]

    # Fill the rest randomly from the combined pool
    all_chars = "".join(pools)
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(all_chars) for _ in range(max(0, remaining))]

    # Shuffle securely
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

# Quick demo if run as script
if __name__ == "__main__":
    print("Example passwords:")
    for L in (12, 16, 24):
        print(f"  {L}: {generate_password(length=L)}")
