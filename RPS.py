import sys

usr1 = input("What's your name? ")
usr2 = input("and, what's your name? ")

usr1_ans = input("%s, do you want to rock, paper or scissor?" % usr1)
usr2_ans = input("%s, do you want to rock, paper or scissor?" % usr2)


def compare(u1, u2):

    if u1 == u2:
        return("Its a tie")
    
    elif u1 == "rock":
        if u2 == "scissor":
            return(f"{usr1} wins!")
        else:
            return(f"{usr2} wins!")
        
    elif u1 == "paper":
        if u2 == "rock":
            return(f"{usr1} wins!")
        else:
            return(f"{usr2} wins!")
    
    elif u1 == "scissor":
        if u2 == "paper":
            return(f"{usr1} wins!")
        else:
            return(f"{usr2} wins!")
    
    else:
        return("Invalid input! You have not entered rock, paper or scissor, try again.")
        sys.exit()

print(compare(usr1_ans, usr2_ans))