import random

computer_input = random.choice(["s", "p", "scr"])
choice_map={"s":1,"p":0,"scr":-1}
reverse_map={1:"Stone",0:"Paper",-1:"scissor"}


user_input=input("Enter your Choice [s for stone,p for paper,scr for scissor:]").lower()

if user_input not in choice_map:
    print("Invalid Input!")
else:
    user_choice=choice_map[user_input]
    computer_choice=choice_map[computer_input]

    print(f"You choose: {reverse_map[user_choice]}")
    print(f"Computer Choose: {reverse_map[computer_choice]}")

    if computer_choice==user_choice:
        print("Its Draw")
    elif(
        (user_choice==1 and computer_choice==-1 ) or
        (user_choice==0 and computer_choice==1 ) or
        (user_choice==-1 and computer_choice==0 )
    ):
        print("You Win") 
    else:
        print("Computer Win") 

