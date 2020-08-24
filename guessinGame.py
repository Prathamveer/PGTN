import random 
  
print("NUMBER GUESSING GAME") 
x = random.randint(1, 10) 
chances = 0
  
print("Guess a number between 1 and 10:")  
while chances < 10: 
    guess = int(input()) 
    if guess == x: 
        print("Congratulations!!! YOU GUESSED THE CORRECT NUMBER") 
        break
    elif guess < x: 
        print("Your guess was too low: Guess a number higher than", guess) 
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
    chances += 1
if not chances < 5: 
    print("You are out of turns.... The number was", x)