import random
import string 
    
string_with_all_characters = list(string.ascii_letters + string.digits + string.punctuation)
digits = list(string.digits)
letters = list(string.ascii_letters)
special_characters = string.punctuation

def generate_password():
    lenght = str(input("Wprowadź ilość liter :"))
    while not lenght.isdigit():
        lenght = str(input("Wprowadź ilość liter :"))
    letters_numbers = str(input("Wprowadź liczbę liter: "))
    while not letters_numbers.isdigit():
        letters_numbers = input("Wprowadź liczbę liter:  ")
    digits_numbers = str(input("Wprowadź ilość liczb :"))
    while not digits_numbers.isdigit():
        digits_numbers = input("Wprowadź ilość liczb: ")
    special_characters_numbers = str(input("Wprowadź ilość znaków specjalnych :"))
    while not special_characters_numbers.isdigit():
        special_characters_numbers = input("Wprowadź ilość znaków specjalnych: ")
    password_number = int(letters_numbers) + int(digits_numbers) + int(special_characters_numbers)
    if (int(password_number) > int(lenght)):
        print("Twoja liczba znaków jest większa od hasła. Wejdź jeszcze raz")
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
        

generate_password()