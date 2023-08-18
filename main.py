alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def ceasar(input_text, shift_amount, direction):
  if direction == 'encode':
    plain_text = input_text
    cipher_text = ''
    for letter in plain_text:
      cipher_text += alphabet[alphabet.index(letter) + shift_amount]       
    print(f'The encoded text is {cipher_text}')
    
  elif direction == 'decode': 
    cipher_text = input_text
    plain_text = ''
    for letter in cipher_text:
      plain_text += alphabet[alphabet.index(letter) - shift_amount]       
    print(f'The decoded text is {plain_text}')

condition = 'yes'
while condition == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction != "encode" or direction != "decode":
    print("Please enter valid function")
  else:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(input_text = text, shift_amount= shift, direction=direction )
    condition = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()