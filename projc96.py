import random

i = 0

num1 = random.randint(0, 9)

while(i < 3):
    
    i+=1
    
    guess = int(input('Guess: '))
    
    if(guess > num1):
        print('Too high!')
        
    
    elif(guess < num1):
        print('Too low!')
        
        
    elif(guess == num1):
        print('You guessed it!')
        i = 4
    
if(i == 3):
    print('You lost!')
