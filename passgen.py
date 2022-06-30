import random
import string

print('Personal Password Generator')

chars = string.ascii_letters +'1234567890!@#$%^&*'

def generate_password():
  length = int(input('Enter length of password: '))
  password = ''
  for i in range(length):
    password = password+random.choice(chars)
  print(password)

generate_password()