alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
string_to_encrypt = input("please enter a message to encrypt: ")
string_to_encrypt = string_to_encrypt.lower()
shift_ammount = int(input("please enter a whole number from 1-25"))
encrypted_string = ""
for current_charachter in string_to_encrypt:
    position = alphabet.find(current_charachter)
    new_position = position + shift_ammount
    if current_charachter in alphabet:
       encrypted_string = encrypted_string + alphabet[new_position]
    else:
        encrypted_string = encrypted_string + current_charachter 
print("your encripted message is", encrypted_string)