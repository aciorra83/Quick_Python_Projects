# random module is going to be used to generate random passwords
import random

print('Welcome to your password generator')
print('=' * 35)
# all possible characters for a strong and unique password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

# user defined input for number of passwords to create, it needs to be a number and not a string
number = int(input('Number of passwords to generate: '))


# user defined password character length, must be a number and not a string
length = int(input('Number of characters in your password: '))

print('\nHere are your password(s):')

# nested for loop, creates number of user defined passwords and password length
for pwd in range(number):
    passwords = ''
    for i in range(length):
# imported random module. choice() method takes the arg of chars and randomly selects the characters of the string
        passwords += random.choice(chars)
    print(passwords)
