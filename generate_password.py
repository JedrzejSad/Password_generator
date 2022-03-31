import random
import string 
    
string_with_all_characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    lenght=str(input("Wprowadź długość hasła: "))
    while not lenght.isdigit():
        lenght = input("Wpisz liczbę: ")
    random.shuffle(string_with_all_characters)
    password=[]
    for i in range(int(lenght)):
        password.append(random.choice(string_with_all_characters))
        
    random.shuffle(password)
    print("Twoje hasło to:")
    print("" .join(password))
        

generate_password()
    

