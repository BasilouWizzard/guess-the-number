import random
print("Hello What's your name?")
name = input()
print('Between what two numbers would you like to guess the magic number' + name + '?')
first = int(input())
last = int(input())
guessTry = 0
number = random.randint(first,last)
while guessTry < number
