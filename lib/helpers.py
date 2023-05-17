from playsound import playsound

from db.models import Genre, Fan

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///genre_app.db')
session = sessionmaker(bind=engine)()

# Create a new fan instance, for the person using our CLI application
def create_fan():
    print("Let's get started!")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    new_fan = Fan(first_name=first_name, last_name=last_name)
    session.add(new_fan)
    print(f'''
    
    Hey {new_fan.first_name} {new_fan.last_name}! We'll ask you some quick questions to help you find a new music genre.
    ''')
    session.commit()

# Run the 4 question quiz that the user interacts with
def assign_genre():
    # QUESTION 1
    print('''

        Question 1: Do you prefer to listen to music while you chill or while you dance?

    ''')
    speed_options = ["1", "2"]
    speed = input('''
        Enter 1 for CHILL or 2 for DANCE: ''')
    while speed not in speed_options:
        speed = input('''
        Please try again. Enter 1 for DANCE or 2 for CHILL: ''')

    if speed == "1":
        speed = 0
    else:
        speed = 106
    print('''
        Thanks for answering - next question!
        ''')

    # QUESTION 2
    print('''

        Question 2: Music can be composed using all different types of sounds! Do you prefer sounds be more instrumental or electronic?
        
    ''')
    style_options = ["1", "2"]
    style = input('''
        Enter 1 for INSTRUMENTAL or 2 for ELECTRONIC: ''')
    while style not in style_options:
        style = input('''
        Please try again, Enter 1 for INSTRUMENTAL or 2 for ELECTRONIC: ''')

    if style == "1":
        style = "Instrumental"
    else:
        style = "Electronic"
    print('''
        Thanks for answering - next question!
        ''')

    # QUESTION 3
    print('''

        Question 3: If you could wake up tomorrow knowing how to play a new instrument, which instrument would it be?
        
    ''')
    instrument_options = ["1", "2", "3"]
    instrument = input('''
        Enter 1 for PIANO, 2 for GUITAR, or 3 for DRUMS: ''')
    while instrument not in instrument_options:
        instrument = input('''
        Please try again. Enter 1 for PIANO, 2 for GUITAR, or 3 for DRUMS: ''')

    if instrument == "1":
        instrument = "Piano"
    elif instrument == "2":
        instrument = "Guitar"
    else:
        instrument = "Drums"
    print('''
        Thanks for answering - one more question!
        ''')

    # Question 4
    print('''

        Question 4: Do you typically follow trends or make trends?
        
    ''')
    commonly_known_options = ["1", "2"]
    commonly_known = input('''
        Enter 1 for TREND FOLLOWER or 2 for TREND SETTER: ''')
    while commonly_known not in commonly_known_options:
        commonly_known = input('''
        Please try again. Enter 1 for TREND FOLLOWER or 2 for TREND SETTER: ''')

    if commonly_known == "1":
        commonly_known = "Yes"
    else:
        commonly_known = "No"
    print('''
        Thanks for answering - that was the last question!
        ''')


    # FILTER
    if speed == 0:
        genres = session.query(Genre).filter(
            (style == Genre.style), (Genre.avg_bpm < 106), (instrument == Genre.prodominent_instrument), (commonly_known == Genre.commonly_known)
        )
    else:
        genres = session.query(Genre).filter(
            (style == Genre.style), (Genre.avg_bpm >= 106), (instrument == Genre.prodominent_instrument), (commonly_known == Genre.commonly_known)
        )

    for genre in genres:
        print(f'''

        You should listen to more.... {genre.name} music!!!!

        ''')

    # Play Audio
    genre_name = genre.name.lower().replace(" ", "_")
    playsound(f"/Users/sarahjones/Desktop/Audio/{genre_name}.mp3")
    # Look into additional way to play audio that doesn't require a computer specific path

    # Create a new review instance. This takes the new fan's id and the id of they genre they've be assigned

