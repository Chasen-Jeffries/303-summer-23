import datetime


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

def decode(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decoded_char = chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decoded_char = char
        decoded_text += decoded_char
    return decoded_text


class BankAccount:
    def __init__(self, name, ID, creation_date, balance):
        self.name == name
        self.ID == ID
        self.creation_date == datetime.date(creation_date)
        self.balance == balance


    def withdrawal (self, amount):
	    self.balance -= amount
                
    def deposit (self, amount):
	    self.balance += amount
            
