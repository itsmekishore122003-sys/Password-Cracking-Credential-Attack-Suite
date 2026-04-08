def generate_dictionary():
    base_words = ["arun", "kumar"]
    numbers = ["123", "2024"]
    symbols = ["@", "#"]

    wordlist = set()
    for word in base_words:
        wordlist.add(word)
        wordlist.add(word.upper())
        wordlist.add(word.capitalize())
        for num in numbers:
            wordlist.add(word + num)
        for sym in symbols:
            wordlist.add(word + sym)

    # Save wordlist
    with open("wordlist.txt", "w") as f:
        for w in wordlist:
            f.write(w + "\n")

    print("Wordlist generated!")

