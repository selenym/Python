import random

print("Welcome to the Rock/Paper/Scissors Game!! Here are the rules of the game:\n","1)It's gonna be 3 rounds.\n","2)You can only choose 1 option per round.\n","3)You write your choice(ex. rock, paper, scissors)\n","4)Winner gets 1 point.\n","5)If it's a draw no one gets a point.")
print("If you read the rules and ready to play Let's Begin!\n")
comp_choice_list=['rock','paper','scissors']
round=1
user_point=0
comp_point=0

while round<=3:
    comp_choice=comp_choice_list[random.randint(0,2)]
    user_choice=input("Write your choice:")
    if user_choice=='rock':
        if comp_choice=='rock':
            print("Comp choice:",comp_choice, "It's a Draw! No one gets a point.")
        if comp_choice=='paper':
            print("Comp choice:",comp_choice, "You Lost! Comp gets a point.")
            comp_point=comp_point+1
        if comp_choice=='scissors':
            print("Comp choice:",comp_choice, "You Win! You get a point.")
            user_point=user_point+1
    if user_choice=='paper':
        if comp_choice=='rock':
            print("Comp choice:",comp_choice, "You Win! You get a point.")
            user_point=user_point+1
        if comp_choice=='paper':
            print("Comp choice:",comp_choice, "It's a Draw! No one gets a point.")
        if comp_choice=='scissors':
            print("Comp choice:",comp_choice, "You Lost! Comp gets a point.")
            comp_point=comp_point+1
    if user_choice=='scissors':
        if comp_choice=='rock':
            print("Comp choice:",comp_choice, "You Lost! Comp gets a point.")
            comp_point=comp_point+1
        if comp_choice=='paper':
            print("Comp choice:",comp_choice, "You Win! You get a point.")
            user_point=user_point+1
        if comp_choice=='scissors':
            print("Comp choice:",comp_choice, "It's a Draw! No one gets a point.")
    round=round+1

print("User's Points:", user_point,"\nComps Points:", comp_point)
if user_point>comp_point:
    print("You Win!")
elif comp_point>user_point:
    print("You Lost! Comp Win!")
else:
    print("It's a Draw. No one Win!")
    



