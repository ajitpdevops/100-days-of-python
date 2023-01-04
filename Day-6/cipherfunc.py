import string
alphabets = list(string.ascii_lowercase)

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabets.index(letter)
        new_position = position + shift
        if new_position > len(alphabets):
            new_position = new_position - len(alphabets)
        cipher_text += alphabets[new_position]
    print(f"The encoded text is:- {cipher_text}")

    # cipher_text = ""
    # for i in range(len(text)):
    #     for position in range(0, len(alphabets)):
    #         if text[i] == alphabets[position]:
    #             new_position = position + shift
    #             if new_position > len(alphabets):
    #                 new_position = new_position - len(alphabets) 
    #             cipher_text += alphabets[new_position]
    # print(f"The encoded text is:- {cipher_text}")

def decrypt(text, shift):
    decipher_text= ""
    for letter in text:
        position = alphabets.index(letter)
        new_position = position - shift
        decipher_text += alphabets[new_position]

    # for i in range(len(text)):
    #     for position in range(0, len(alphabets)):
    #         if text[i] == alphabets[position]:
    #             new_position = position - shift
    #             decipher_letter = alphabets[new_position]
    #             decipher_text_list.append(decipher_letter)
    # decipher_text = "".join(letter for letter in decipher_text_list)

    print(f"The decoded text is:- {decipher_text}")    


def caeser(text, shift, direction):
    final_text = ""
    for letter in text:
        if letter in alphabets: 
            position = alphabets.index(letter)
            if direction == 'encode':
                new_position = position + shift
                if new_position >= len(alphabets):
                    new_position = new_position % len(alphabets)
            elif direction == 'decode':
                new_position = position - shift
            else:
                print("Invalid direction input")
            final_text += alphabets[new_position]
        else:
            final_text += letter
    print(f"The {direction}d text:- {final_text}")
