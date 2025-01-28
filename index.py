first_contestant = None
second_contestant = None
first_contestant_vote = 0
second_contestant_vote = 0
def voting_app():
    print("Welcome to our polls")
    handle_contestants()
    vote_contestant()
    announce_winner()

    

def handle_contestants():
    global first_contestant, second_contestant
    first_contestant = input("Enter the first contestant name: ")
    print(f"{first_contestant} added successfully")
    second_contestant = input("Enter the second contestant name: ")
    print(f"{second_contestant} added successfully")

def vote_contestant():
    global first_contestant, second_contestant, first_contestant_vote, second_contestant_vote
    print("Which contenstant are you voting for?")
    voter_choice = input(f"1. {first_contestant} 2. {second_contestant}: ")
    if(voter_choice == "1"):
        first_contestant_vote = first_contestant_vote + 1
    elif(voter_choice == "2"):
        second_contestant_vote = second_contestant_vote + 1
    else:
        print("Invalid vote")
    print("Do you want to vote again?")
    vote_again = input("1. Yes 2. No: ")
    if(vote_again == "1"):
        vote_contestant()
    else:
        print("Thanks for voting.")
    

def announce_winner():
    if(first_contestant_vote > second_contestant_vote):
        print(f"{first_contestant} won {second_contestant} with {first_contestant_vote} to {second_contestant_vote}")
    elif(second_contestant_vote > first_contestant_vote):
        print(f"{second_contestant} won {first_contestant} with {second_contestant_vote} to {first_contestant_vote}")
    elif(first_contestant_vote == second_contestant_vote):
        print(f"Both {first_contestant} and {second_contestant} have {first_contestant_vote}, hence, NO WINNER")

    

voting_app()
