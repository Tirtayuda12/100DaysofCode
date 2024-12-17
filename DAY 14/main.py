from game_data import data
from art import logo,vs
import random
#print the logo
print(logo)
score = 0

game_should_continue = True
#Make game repeatable
while game_should_continue:
    #create function to generate random choice in the list of data
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    def format_data(account):
        # Format the account data into printable format
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"
    
    def check_guess(guess,a_followers,b_followers):
        #check the guess
        if a_followers > b_followers:
            if guess == 'a':
                return True
            else:
                return False
        else:
            if guess == 'b':
                return True
            else:
                return False
        
                

    print(f"Compare A:{format_data(account_a)}.")
    print(vs)
    print(f"Against B:{format_data(account_b)}.")
    #Ask user for the guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    ## get the follower count
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_guess(guess,a_follower,b_follower)

    #Give user a feedback on their guess.
    if is_correct:
        score+=1
        print(f"Youre right! Current score:{score}")
    else:
        game_should_continue = False
        print(f"Sorry, thats wrong. Final score:{score}")











    
