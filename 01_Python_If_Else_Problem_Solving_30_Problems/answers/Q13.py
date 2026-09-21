inp=input("Enter the Single letter : ").strip()
if "a"<=inp<="z" or "A"<=inp<="Z":
    if inp.lower() in ("a","e","i","o","u") :
        print("Character Entered is a Vowel")
    else:
        print("Character Entered is a consonant")
else:
    print("Invalid Input")
