import itertools
import hashlib
import string

def brute_force(hash_to_crack, max_length=3):
    chars = string.ascii_lowercase + string.digits
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt)
            if hashlib.sha256(attempt.encode()).hexdigest() == hash_to_crack:
                return attempt
    return None
