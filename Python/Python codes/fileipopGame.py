'''The game() function in a program lets a user play a game and returns the score as an integer.
 You need to read a file Hi-score.txt which is either blank or contains the previous Hi-score. 
 You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.'''
import random

def game():
    print("You are Playing a Game:")
    score=random.randint(1,150)
    # fetch this score
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    
    print(f"Your score is {score}")
    if score > hiscore:
        print("🎉 New High Score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"High Score remains: {hiscore}")
    return score

game()


