from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import (assign_genre, create_fan, create_review, average_review, Colors)

engine = create_engine('sqlite:///genre_app.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print(Colors.cyan, f'''
    
Welcome to...
    ''')
    print(f'''

    
 /$$      /$$                     /$$                  /$$$$$$                                                 /$$$$$$            /$$           /$$
| $$$    /$$$                    |__/                 /$$__  $$                                               /$$__  $$          |__/          | $$
| $$$$  /$$$$ /$$   /$$  /$$$$$$$ /$$  /$$$$$$$      | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$ /$$   /$$ /$$ /$$$$$$$$| $$
| $$ $$/$$ $$| $$  | $$ /$$_____/| $$ /$$_____/      | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$      | $$  | $$| $$  | $$| $$|____ /$$/| $$
| $$  $$$| $$| $$  | $$|  $$$$$$ | $$| $$            | $$|_  $$| $$$$$$$$| $$  \ $$| $$  \__/| $$$$$$$$      | $$  | $$| $$  | $$| $$   /$$$$/ |__/
| $$\  $ | $$| $$  | $$ \____  $$| $$| $$            | $$  \ $$| $$_____/| $$  | $$| $$      | $$_____/      | $$/$$ $$| $$  | $$| $$  /$$__/      
| $$ \/  | $$|  $$$$$$/ /$$$$$$$/| $$|  $$$$$$$      |  $$$$$$/|  $$$$$$$| $$  | $$| $$      |  $$$$$$$      |  $$$$$$/|  $$$$$$/| $$ /$$$$$$$$ /$$
|__/     |__/ \______/ |_______/ |__/ \_______/       \______/  \_______/|__/  |__/|__/       \_______/       \____ $$$ \______/ |__/|________/|__/


        ''')
    
    game_running = True
    while game_running:
        # Create a new fan instance, for the person using our CLI application
        create_fan()

        # Run the 4 question quiz that the user interacts with
        assign_genre()

        # Create a new review instance. This takes the new fan's id and the id of they genre they've be assigned
        create_review()

        # Pull the average star rating for the genre the new fan just reviewed
        average_review()

        choice_options = ["1", "2"]
        last_choice = input('''
        Thank you for using the Music Genre Quiz! Enter 1 to QUIT or 2 to PLAY AGAIN: ''')

        while last_choice not in choice_options:
            last_choice = input('''
        Enter 1 to QUIT or 2 to PLAY AGAIN: ''')
            
        if last_choice == "1":
            print('''
            
        All done!
            ''')
            game_running = False
        else:
            game_running = True

