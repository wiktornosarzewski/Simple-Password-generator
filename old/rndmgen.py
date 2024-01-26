import random

def rand_string(length):
	str = ""
	chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	size = len(chars)
	for i in range(length):
		str = chars[random.randint( 0, size - 1 )]
        print(random.randint(1, 100))
        return str


mypass = rand_string(10)

#print(random.randint(1, 100))
