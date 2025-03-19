import random
import string 

def generated_password(length=12):
    charactors = string.ascii_letters + string.digits + string.punctuation + string.hexdigits
    password = ''.join(random.choice(charactors) for _ in range(length))
    return password

#User  inputs 
length = int(input ("Enter the length of your desired password:"))
password = generated_password(length)
print("Your desired Generated Password:", password)
