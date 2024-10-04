def encrypt(original_text: str, shift_amount: int) -> None:

    new_text = ""

    for char in original_text:
            new_position = (alphabet.index(char) + shift_amount) % 26
            new_text += alphabet[new_position]

    print(new_text)

def decrypt(original_text: str, shift_amount: int) -> None:
     
    new_text = ""

    for char in original_text:
        new_position = (alphabet.index(char) - shift_amount) % 26
        new_text += alphabet[new_position]

    print(new_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt a message, type 'decode' to decrypt:\n").lower()

text : str = input("Please type your message:\n").lower()
shift = int(input ("Please type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)




