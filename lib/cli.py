from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import (create_new_fan)

engine = create_engine('sqlite:///db/genre_app.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print(f'''

        Welcome to my Genre CLI!

        ''')
    
    # Create a new fan instance, for the person using our CLI application
    welcome_new_fan = create_new_fan()
    print(welcome_new_fan)