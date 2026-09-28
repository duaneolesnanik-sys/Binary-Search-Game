import random

def user_input(min = "", max = "", question = str): 
    """gets user input within given parameters and returns the first valid answer"""
    while True: 
        guess = input(question).strip() 
        if min == "" and max == "" and guess.isdigit(): 
            break 
        elif min == "" and guess.isdigit() and int(guess) <= int(max): 
            break 
        elif max == "" and guess.isdigit() and int(guess) >= int(min): 
            break  
        elif guess.isdigit() and int(guess)<=int(max) and int(guess)>=int(min): 
            break 
        else: 
            print("Invalid Guess") 
    return int(guess)

def result(guess, target): 
    """Checks whether the guess is too high, too low, or correct"""
    if guess > target: 
        print("Too High") 
        return "high" 
    elif guess < target: 
        print("Too Low") 
        return "low"
    else: 
        print("That's the Number.") 
        return "correct"

def mid_num(min,max): 
    """Gives the optimal guess using binary search"""
    print(f"Low: {min}\nHigh: {max}") 
    print(f"({min}+{max}) // 2 = {(min+max)//2}") 
    print(f"Computer Guess:  {(min+max)//2}") 
    return (min+max)//2

def end_info(pguess,cguess, target):
    """Prints the end results and who the winner is.""" 
    print("-"*12,"Final Results","-"*12) 
    print(f"\nTarget number: {target}") 
    print(f"\nPlayer Guesses:\n{pguess}\nPlayer Guess Count: {len(pguess)}") 
    print(f"\nComputerer Guesses:\n{cguess}\nComputer Guess Count: {len(cguess)}") 
    print("Winner: Player" if len(cguess)>=len(pguess) else "Winner: Computer") 
    print("-"*18) 

def comp_guessing(min_num, max_num, target):
    """Takes computer guesses and returns a list of them"""
    min_guess = min_num
    max_guess = max_num
    cguess = []
    while True:
            guess = mid_num(min_guess,max_guess)
            rguess = result(guess,target)
            cguess.append(guess)
            if rguess == "correct":
                break
            elif rguess == "high" and guess < max_guess:
                max_guess = guess
            elif rguess == "low" and guess > min_guess:
                min_guess = guess
    return(cguess)

def play_guessing(min_num, max_num, target):
    """Takes player guesses and returns a list of them"""
    pguess = []
    while True:
            guess = user_input(min_num, max_num, "Take a guess: ")
            pguess.append(guess)
            if result(guess, target) == "correct":
                break
    return(pguess)

while True:
    min_num = user_input(question = "What is the minimum value: ")
    max_num = user_input(min_num, question = "What is the maximum value: ")
    target = random.randint(min_num,max_num)
    pguess = []
    cguess = []
    pguess = play_guessing(min_num, max_num, target)
    cguess = comp_guessing(min_num, max_num, target)
    end_info(pguess, cguess, target)
    if not input("Type p to play again: ").strip().lower() == "p":
        break
