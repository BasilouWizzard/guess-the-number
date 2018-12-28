import random,math
print("Hello What's your name?")
name = input()
print('Between what two numbers would you like to guess the magic number' + name + '?')
first = int(input())
last = int(input())
guessTry = 0
number = random.randint(first,last)
tries = int(2*(math.log((last - first) , 2)))
while guessTry < tries :
  print("Take a guess!  " + str(tries - guessTry) +" tries remaining !")
  guess = int(input())
  if guess < number :
    print('Too low, try again !')
  if guess > number :
    print('Too high, try again !')
  guessTry = guessTry + 1 
  if guess == number :
    break;
print('Well done!')
print('you guessed the magic number in ' + str(guessTry) + ' tries !')
