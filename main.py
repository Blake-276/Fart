try:
    # this encryptor only supports text and numbers

    import winsound

    letters = {
        "A": "brr",
        "B": "fuss",
        "C": "puii",
        "D": "purr",
        "E": "bharr",
        "F": "trrr",
        "G": "puak",
        "H": "bhuakka",
        "I": "bhyatta",
        "J": "parakka",
        "K": "sss",
        "L": "prrr",
        "M": "grrr",
        "N": "durr",
        "O": "farr",
        "P": "blat",
        "Q": "braaap",
        "R": "THPPTPHTP",
        "S": "BLAAARP",
        "T": "PFFT",
        "U": "braack",
        "V": "fraaa",
        "W": "krrrt",
        "X": "toot",
        "Y": "boom",
        "Z": "bratta",
        " ": "ptrr"
    }


    def encrypt(text):
        encrypted_text = "@"
        for i in text:
            if i.upper() in letters:
                encrypted_text += letters[i.upper()]
            if i == " ":
                encrypted_text += "ptrr"
        return encrypted_text


    def play_sound(decryptext):
        array = list(decryptext)
        for i in array:
            print(letters[i.upper()])
            winsound.PlaySound(f'F_sounds\{letters[i.upper()]}.wav',
                               winsound.SND_LOOP)


    def decrypt(text):
        word = ""
        word_array = list(text)
        word_array.remove("@")
        decrypt_values = list(letters.values())
        decrypt_keys = list(letters.keys())
        print(decrypt_keys)
        print(decrypt_values)
        decrypted_value = ""

        for i in word_array:

            if word in decrypt_values:
                decrypted_value += decrypt_keys[decrypt_values.index(word)]
                word = ""
                word += i
            elif word == "ptrr":
                decrypted_value += " "
                word = ""
                word += i
            else:
                word += i
            print(word)

        return decrypted_value


    input_text = input("enter_encrypted_text_to_decrypt_or_text_needed_to_encrypt:")

    if input_text[0] == "@":
        print("decrypted_text: ")
        print(decrypt(input_text + " "))
    else:
        print("encrypted_text: ")
        print(encrypt(input_text))
        play_sound(input_text)
except:
    print("error")
