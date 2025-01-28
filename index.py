def voting_app():
    print("Welcome to our polls")
    handle_contestants()
    

def handle_contestants():
    first_contestant = input("Enter the first contestant name: ")
    print(f"{first_contestant} added successfully")
    second_contestant = input("Enter the second contestant name: ")
    print(f"{second_contestant} added successfully")
    
voting_app()
