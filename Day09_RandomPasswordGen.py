import random 
import string
size = int(input('Enter the password Length: '))
print('''
Enter Choice :- 
    1. digits
    2. Letters
    3. Special characters
    4. Exit
''')
CharList = ''
while True:
    choice = input('Pick a Number: ')
    if choice == '1':
        CharList += string.digits
    elif choice == '2':
        CharList += string.ascii_letters
    elif choice == '3':
        CharList += string.punctuation
    elif choice == '4':
        break
    else:
        print('Invalid Number!')
password = ''
for i in range(size):
    password += random.choice(CharList)
print("The random password is ", password)
