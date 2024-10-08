from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + shift_amount
            new_letter = alphabet[new_pos]
            end_text += new_letter
        else:
            end_text += char
            
        
    print(f"The {cipher_direction}d text is {end_text}.")

end = False
while not end:
    action = input("Type 'encode' to encrypt and 'decode' to decrypt : ")
    text = input("Enter a message : ").lower()
    shift = int(input("Enter the amount of shift : "))
    shift = shift % 26

    caesar(start_text = text,shift_amount = shift,cipher_direction = action)

    restart = input("Do you want to continue again? Type yes or else type no : ")
    if restart == "no":
        end = True
        print("Goodbye")