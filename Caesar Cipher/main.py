from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(original_text, shift_amount, encode_or_decode):
    # encryption
    if encode_or_decode == "encode":
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cipher_text+=letter
            else:
                alpha_ind=(alphabet.index(letter)+shift_amount)%len(alphabet) #index int
                cipher_text += alphabet[alpha_ind]
        print(cipher_text)
    #decryption
    elif encode_or_decode == "decode":
        original_data = ""
        for letter in original_text:
            if letter not in alphabet:
                original_data+=letter
            else:
                org_ind=alphabet.index(letter) - shift_amount
                if org_ind<0:
                    alpha_ind=len(alphabet)+org_ind
                else:
                    alpha_ind = (alphabet.index(letter) - shift_amount) % len(alphabet)  # index int
                original_data += alphabet[alpha_ind]
        print(original_data)

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart= input("Type yes to continue or else type no to exit:\n")
    if restart=="no":
        should_continue=False
        print("Exited")