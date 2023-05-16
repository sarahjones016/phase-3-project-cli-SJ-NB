from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import (assign_genre)
from db.models import Fan

engine = create_engine('sqlite:///genre_app.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print(f'''

        Welcome to my Genre CLI!

        ''')
    
    # Create a new fan instance, for the person using our CLI application
    print("Let's get started!")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    new_fan = Fan(first_name=first_name, last_name=last_name)
    session.add(new_fan)
    print(f'''
    
    Hey {new_fan.first_name} {new_fan.last_name}! We'll ask you some quick questions to help you find a new genre
    ''')
    session.commit()


    # Run the 4 question quiz that the user interacts with
    assign_genre()

