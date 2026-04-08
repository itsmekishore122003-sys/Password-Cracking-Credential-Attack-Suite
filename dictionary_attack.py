import hashlib

def dictionary_attack(hash_to_crack):
    with open("wordlist.txt", "r") as f:
        words = f.read().splitlines()

    for word in words:
        if hashlib.sha256(word.encode()).hexdigest() == hash_to_crack:
            return word
    return None
