def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted = ord(char) + shift

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26  
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26  
                elif shifted < ord('A'):
                    shifted += 26  

            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)  

input_text = "BMS College of Engineering"
shift_amount = 5

encrypted = encrypt(input_text, shift_amount)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift_amount)
print("Decrypted:", decrypted)
