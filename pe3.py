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
        if creation_date > datetime.date.today():
            raise Exception("Invalid creation date, must be present or past date")
        
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def withdraw(self, amount):
	    self.balance -= amount
        
    def deposit(self, amount):
	    self.balance += amount

    def view_balance(self):
	    return self.balance
            
class SavingsAccount(BankAccount):
    def __init__(self, name, ID, creation_date, balance):
        super().__init__(name, ID, creation_date, balance)
        self.waiting_period = creation_date + datetime.timedelta(days=180)

    def withdraw(self, amount):
        if datetime.date.today() < self.waiting_period:
            print("Unable to withdraw money due to the six month waiting period after account creation.")
        else:
            if amount <= self.balance:
                super().withdraw(amount)
            else: 
                print("Unable to overdraft, the maximum withdraw amount for your account is:")
                return super().view_balance()

class CheckingAccount(BankAccount):
    def __init__(self, name, ID, creation_date, balance):
         super().__init__(name, ID, creation_date, balance)
    
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 30 # penalty fee
        super().withdraw(amount)
