import pickle
import time
import gambling_wordle


FILENAME = 'user_detail.dat'

def load_all_users():
    try:
        with open(FILENAME, 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

def save_all_users(user_list):
    with open(FILENAME, 'wb') as f:
        pickle.dump(user_list, f)

def signup(users):
    print("\n--- Create New Account ---")
    while True:
        name = input("Enter new username: ")
        # Check if name already exists
        if any(u[0] == name for u in users):
            print("That name is already taken! Choose another.")
            continue
        
        passwd = input("Create password (8+ characters): ")
        if len(passwd) < 8:
            print("Password too short!")
            continue
        
        # Add to the list and save back to file
        users.append([name, passwd])
        save_all_users(users)
        
        # progressBar Animation
        for i in range(21):
            bar = '#' * i + '-' * (20 - i)
            print(f"[{bar}] {i*5}%", end='\r')    
            time.sleep(0.1)
        
        print("\nSignup Successful!")
        gambling_wordle.start_game()
        break

def login():
    users = load_all_users()
    print("Welcome to the Game")
    name = input("Enter name: ")

    # Find if user exists in the list of lists
    found_user = next((u for u in users if u[0] == name), None)
    '''next() - finds a match (e.g., 'alice'), it pulls out that entire sub-list: ['alice', 'pass123']
                return None if no matches found'''
    
    if found_user:  #True value if not empty 
        # User exists, check password
        while True: #While to give infinte attempts for password , if user got it wrong by mistake
            passwd = input("Enter password: ")
            if passwd == found_user[1]:


                #dot dot dot animation
                for i in range(8):
                    # This cycles through 1, 2, 3 dots using the modulo (%) operator
                    dots = "." * (i % 3 + 1)
                    print(f"loggin in{dots:<3}", end="\r")
                    time.sleep(0.3)


                time.sleep(0.1)  #prints the next like 0.1 sec late to depict loading action
                print("Successfully logged in...")
                gambling_wordle.start_game() # Start the game!
                break
            else:
                retry = input("Incorrect password! Try again? (y/n): ").lower()
                if retry != 'y':
                    break
    else:
        # User does not exist
        print("Name not found.")
        signup(users)

if __name__ == "__main__":
    login()