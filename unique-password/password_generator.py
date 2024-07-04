"""
    Dynamically Generated 
          Unique Password
        -- user can set length of password (min 7 chars)
        -- user selects if they want it to contain 
            special characters & numbers

        use random and string modules
            -- use string to grab all chars, 
                -- including special chars & nums
"""
import random
import string

print()
print('Welcome to Unique Password')
print('Creating dynamically generated passwords. \n')

def generate_password(min_length, numbers=True, special_characters=True) :
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation   
    characters = letters  
    if numbers :
        characters += digits       
    if special_characters :
        characters += special
    pwd = ''
    meets_criteria = False 
    has_number = False
    has_special = False
    while not meets_criteria or len(pwd) < min_length :
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits :
            has_number = True     
        elif new_char in special :
            has_special = True
        meets_criteria = True
        if numbers :
            meets_criteria = has_number
        if special_characters :
            meets_criteria = meets_criteria and has_special  
    return pwd    

def create_pwd() :
    create = input('Would you like to generate an new password: (y/n)  ').lower() == 'y'
    if create == True :
        min_length = int(input('Enter the minimum length of password:  '))
        has_number = input('Do you want to have numbers in password? (y/n)  ').lower() == 'y'
        has_special = input('Do you want to have special characters in password? (y/n)  ').lower() == 'y'
        pwd = generate_password(min_length, has_number, has_special)
        print(f'Unique Password: {pwd} \n')
        create_pwd()
    else :
        print('Thank you for using a Unique Password - dynamically-generated, password generator.')

create_pwd()
print()
