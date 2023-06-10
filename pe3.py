import datetime
import string

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

def decode(input_text, shift):
    decoded_text = ""
    for char in input_text:
        if char.isalpha():
            if char.islower():
                decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decoded_text += decoded_char
        else:
            decoded_text += char        
    return decoded_text

class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=datetime.date.today(), balance=0):
        if creation_date > datetime.date.today():
            raise Exception("Invalid creation date, must be present or past date")
        
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -= amount
        else:
            print('You have insufficient funds')

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print('You must select a postive number as your deposit amount')

    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name, ID, creation_date, balance):
        super().__init__(name, ID, creation_date, balance)
        self.waiting_period = creation_date + datetime.timedelta(days=180)

    def withdraw(self, amount):
        if datetime.date.today() < self.waiting_period:
            raise Exception("Unable to withdraw money due to the six month waiting period after account creation.")
        else:
            if amount >= 0:
                if amount <= self.balance:
                    self.balance -= amount
                else: 
                    raise Exception("Unable to withdraw due to overdraft (insufficient funds)")
            else:
                raise Exception("You must select a positive number as your withdraw amount")
            
class CheckingAccount(BankAccount):
    def __init__(self, name, ID, creation_date, balance):
         super().__init__(name, ID, creation_date, balance)
    
    def withdraw(self, amount):
        if amount >= 0:
            if self.balance >= amount:
                self.balance -= amount
            else:    
                self.balance -= 30 # penalty fee
                print("insufficient funds, overdraft fee applied")            
        else:
            print("You must select a positive number as your withdraw amount")