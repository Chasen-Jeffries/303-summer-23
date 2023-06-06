def encode (input_text, shift):
    alphabet = [chr(ord('a') + i) for i in range(26)]
    encoded_text = ""
    for char in input_text.lower():
            if char.isalpha():
                  index = (ord(char) - ord('a') + shift) % 26
                  encoded_text += alphabet[index]
            else:
                  encoded_text += char
    return alphabet, encoded_text





                  
