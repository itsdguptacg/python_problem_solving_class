inp=input("Enter the Single letter : ").strip()
if "A"<=inp<="Z":
    print("Character Entered is a Upper Case alphabet")
elif "a"<=inp<="z":
    print("Character Entered is a Lower Case alphabet")
elif "0"<=inp<="9":
    print("Character Entered is a Digit")
else:
    print("Character Entered is a Special Character")
