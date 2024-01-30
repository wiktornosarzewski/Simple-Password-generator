import random
import string

def rand_string(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))

mypass = rand_string(10)
mypass2 = rand_string(8)
print(mypass)
print(" ")
print(mypass2)
input()
