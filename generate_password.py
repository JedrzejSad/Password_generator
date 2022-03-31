import random
import string 
    
string_with_all_characters = list(string.ascii_letters + string.digits + string.punctuation)
digits = list(string.digits)
letters = list(string.ascii_letters)
special_characters = string.punctuation

def generate_password():
    lenght = str(input("Enter password lenght:"))
    while not lenght.isdigit():
        lenght = str(input("Enter password lenght:"))
    letters_numbers = str(input("Enter  amount of letters: "))
    while not letters_numbers.isdigit():
        letters_numbers = input("Enter amount of letters :  ")
    digits_numbers = str(input("Enter amount of digits :"))
    while not digits_numbers.isdigit():
        digits_numbers = input("Enter amount of digits: ")
    special_characters_numbers = str(input("Enter amount of special characters :"))
    while not special_characters_numbers.isdigit():
        special_characters_numbers = input("Enter amount of special characters: ")
    password_number = int(letters_numbers) + int(digits_numbers) + int(special_characters_numbers)
    if (int(password_number) > int(lenght)):
        print("Your amount of characters is longer than password. Choose again.")
        return
    random.shuffle(string_with_all_characters)
    password=[]
    for i in range(int(letters_numbers)):
        password.append(random.choice(letters))
    for i in range(int(digits_numbers)):
        password.append(random.choice(digits))
    for i in range(int(special_characters_numbers)):
        password.append(random.choice(special_characters))
    for i in range(int(int(lenght) - password_number)):
        password.append(random.choice(string_with_all_characters))
        
    random.shuffle(password)
    print("Your password:")
    print("" .join(password))
        

generate_password()9