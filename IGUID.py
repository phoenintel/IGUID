import random
from datetime import datetime

def generer_identifiant(initials, CC, internal_level, date, temporary_member):
    # generate id number
    nombre_accroche = f'{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}'

    # Title
    print('===================\n==IGUID generator==\n===================\n')
    print('This work is licensed under a CC BY-NC-SA 4.0 License. Read it here: https://creativecommons.org/licenses/by-nc-sa/4.0/')
    print('Source code: https://github.com/phoenintel/IGUID\n')
    
    # Enter your ID info here
    initials = input('Enter your initials in uppercase letters (the first letter of your surname and the first letter of your first name): ')
    CC = input('Enter your country code in uppercase letters (e.g. US for united states): ') 
    internal_level = input('Enter your infrastructure level (see documentation for more information): ')
    member_number = input("Enter your member number (if necessary, ask the administration for it, if your don't know your member number, don't worry, enter the letter N in upper case): ")

    # Generate date with JJ.MM.AA format
    date = date.strftime("%d.%m.%y")

    # Générer la valeur membre temporaire
    temporary_member_value = input('Enter the number of membership days. If this value is permanent, enter the letter N in upper case: ') if not temporary_member else str(temporary_member)

    # generate PIN code relied to ID
    code_pin = f'{random.randint(1000, 9999)}'

    # Construire l'identifiant final
    identifiant = f'{nombre_accroche}-{initials}-{CC}-{internal_level}-{member_number}-{date}-{temporary_member_value}-{code_pin}'
    
    return identifiant

# Variables
initials = "initials"
CC = "US"
internal_level = 5
date = datetime(2023, 10, 31)
temporary_member = False

identifiant = generer_identifiant(initials, CC, internal_level, date, temporary_member)
print(identifiant)