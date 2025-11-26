def count(text: str):
    digits = 0
    letters = 0
    upper = 0
    lower = 0
    spaces = 0
    symbols = 0
    vowels = 0
    consonants = 0

    ukraine = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    english = "aeiouAEIOU"
    symbol = ".?,<>\/|{}[]-=+()*&^:;%$#@!~`№"

    for i in text:

        if i == " ":
            spaces += 1

        if i.isdigit():
            digits += 1

        if i in symbol:
            symbols += 1

        if i.isalpha():
            letters += 1

            if i.isupper():
                upper += 1
            else:
                lower += 1

            if i in ukraine or i in english:
                vowels += 1
            else:
                consonants += 1

    return {
        "Digits": digits,
        "Letters": letters,
        "Upper": upper,
        "Lower": lower,
        "Spaces": spaces,
        "Symbols": symbols,
        "Vowel": vowels,
        "Consonant": consonants
    }

print(count('Some text 123.'))