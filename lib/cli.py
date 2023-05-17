from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import (assign_genre, create_fan)
from db.models import Fan

engine = create_engine('sqlite:///genre_app.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print(f'''
    
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
    
    # Create a new fan instance, for the person using our CLI application
    create_fan()


    # Run the 4 question quiz that the user interacts with
    assign_genre()

    # Create a new review instance. This takes the new fan's id and the id of they genre they've be assigned

