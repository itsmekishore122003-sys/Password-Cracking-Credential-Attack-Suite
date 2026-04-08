from dictionary.generator import generate_dictionary
import hashing.hash_module as hs
import attack.dictionary_attack as da
import attack.bruteforce as bf
import analysis.strength as st
import report.report as rp

def main():
    print("STEP 1: Generating dictionary...")
    generate_dictionary()   # ✅ Call directly

    password = input("Enter password to test: ")

    print("STEP 2: Hashing password...")
    hashed = hs.hash_password(password)

    with open("hash.txt", "w") as f:
        f.write(hashed)

    print("STEP 3: Dictionary attack...")
    result = da.dictionary_attack(hashed)
    print("Dictionary cracked:" , result if result else "Failed")

    print("STEP 4: Brute-force attack...")
    brute = bf.brute_force(hashed)
    print("Brute-force cracked:" , brute if brute else "Failed")

    print("STEP 5: Checking strength...")
    strength = st.check_strength(password)
    print("Strength:", strength)

    print("STEP 6: Generating report...")
    rp.generate_report(password, strength)

if __name__ == "__main__":
    main()
