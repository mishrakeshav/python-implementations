import math
import string
from typing import List

def calculate_rolling_hash(word):
    MOD = 10 ** 9 + 7
    P = 256
    curr = 0
    for w in word:
        curr = (curr*P + ord(w))%MOD
    return curr

def calculate_reverse_rolling_hash(word):
    MOD = 10 ** 9 + 7
    P = 256
    p = 1
    curr = 0
    for w in word:
        curr = (curr + p*ord(w)) % MOD
        p *= P
    return curr


################## get substring hash ##################

def precompute_hashes(s: str, p: int = 31, mod: int = 10 ** 9 + 7):
    n = len(s)
    prefix_hashes = [0] * (n + 1)
    p_powers = [1] * (n + 1)

    # Precompute powers of p (i.e., p^0, p^1, p^2, ..., p^n) modulo mod
    for i in range(1, n + 1):
        p_powers[i] = (p_powers[i - 1] * p) % mod

    # Precompute prefix hashes
    for i in range(n):
        prefix_hashes[i + 1] = (prefix_hashes[i] + (ord(s[i]) - ord('a') + 1) * p_powers[i]) % mod

    return prefix_hashes, p_powers


def get_substring_hash(l: int, r: int, prefix_hashes, p_powers, mod: int = 10 ** 9 + 7):
    # Hash of substring s[l:r+1] using the prefix hashes
    hash_value = (prefix_hashes[r + 1] - prefix_hashes[l] + mod) % mod
    # Normalize by dividing by p^(l), i.e., multiplying by the modular inverse of p^l
    # pow(p_powers[l], mod - 2, mod) calculated module inverse of p^l
    # Proof :
    # module inverse of (a⋅b) mod m = 1
    # fermat's little theorem : if m is a prime number then a ^ (m - 1) = 1 mod m
    # => a ^ (m - 2) = a^(-1) mod m
    # so by calculating pow(p_powers[l], mod - 2, mod) we get module inverse of (p^l)
    return (hash_value * pow(p_powers[l], mod - 2, mod)) % mod

################## ----------------- ##################




def rabin_karp(pattern: str, text: str) -> List[int]:
    prime_base = 31
    mod = int(1e9 + 9)
    pattern_len, text_len = len(pattern), len(text)

    # Precompute powers of prime_base modulo mod
    prime_powers = [1] * max(pattern_len, text_len)
    for i in range(1, len(prime_powers)):
        prime_powers[i] = (prime_powers[i - 1] * prime_base) % mod

    # Compute prefix hashes for the text
    text_hashes = [0] * (text_len + 1)
    for i in range(text_len):
        text_hashes[i + 1] = (text_hashes[i] + (ord(text[i]) - ord('a') + 1) * prime_powers[i]) % mod

    # Compute the hash for the pattern
    pattern_hash = 0
    for i in range(pattern_len):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * prime_powers[i]) % mod

    occurrences = []
    for i in range(text_len - pattern_len + 1):
        # Get current substring hash
        current_hash = (text_hashes[i + pattern_len] - text_hashes[i] + mod) % mod
        # Compare it with the pattern hash
        # the current_hash need to be multiplied by module inverse of prime_powers[i] to get the correct hash
        # instead of that we multiply pattern_hash by prime_powers[i] for comparison
        if current_hash == (pattern_hash * prime_powers[i]) % mod:
            occurrences.append(i)

    return occurrences



        