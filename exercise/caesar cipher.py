alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:                   #if are used because when we used special symbol then it is ajitiz
            position = alphabet.index(char)
            new_position = (position+shift_key)%26
            cipher_text +=alphabet[new_position]
        else:
            cipher_text +=char
    print(f"here is the text after encryption : {cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position-shift_key)%26
            plain_text +=alphabet[new_position]
        else:
             plain_text +=char
    print(f"here is the text after decryption : {plain_text}")


end_program = False
while not end_program:
      what_to_do = input("type 'encrypt' for encryption, type 'decrypt' for decryption :\n")
      text = input("type your message: \n").lower()
      shift = int(input("enter shift key: \n"))

      if what_to_do == "encrypt":
           encryption(text,shift)
      elif what_to_do == "decrypt":
         decryption(text,shift)
      play_again = input("type 'yes' to continue, type 'no' to exit \n")
      if play_again =='no':
          end_program = True
          print("have a nice day ! bye bye")

'''type 'encrypt' for encryption, type 'decrypt' for decryption :
encrypt
type your message: 
hello *
enter shift key: 
3
here is the text after encryption : khoor *
type 'yes' to continue, type 'no' to exit 
yes
type 'encrypt' for encryption, type 'decrypt' for decryption :
decrypt
type your message: 
khoor *
enter shift key: 
3
here is the text after decryption : hello *
type 'yes' to continue, type 'no' to exit 
no
have a nice day ! bye bye'''