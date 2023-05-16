from db.models import Fan, Genre

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///genre_app.db')
session = sessionmaker(bind=engine)()

def assign_genre():
    # QUESTION 1
    print('''

        Question 1: Do you prefer to listen to music while you chill or while you dance?

    ''')
    speed_options = ["1", "2"]
    speed = input("Enter 1 for CHILL or 2 for DANCE: ")
    while speed not in speed_options:
        speed = input("Please try again. Enter 1 for DANCE or 2 for CHILL: ")

    if speed == "1":
        speed = 0
    else:
        speed = 106
    print("Thanks for answering - next question!")
    # print(f"INTERNAL STATUS OF SPEED: {speed}")

    # QUESTION 2
    print('''

        Question 2: Music comes in ALL different sounds! Do you prefer those sounds be more instrumental or more electronic?
        
    ''')
    style_options = ["1", "2"]
    style = input("Enter 1 for INSTRUMENTAL or 2 for ELECTRONIC: ")
    while style not in style_options:
        style = input("Please try again, Enter 1 for INSTRUMENTAL or 2 for ELECTRONIC: ")

    if style == "1":
        style = "Instrumental"
    else:
        style = "Electronic"
    print("Thanks for answering - next question!")
    # print(f"INTERNAL STATUS OF STYLE: {style}")

    # QUESTION 3
    print('''

        Question 3: If you could wake up tomorrow knowing how to play a new instrument, which would it be?
        
    ''')
    instrument_options = ["1", "2", "3"]
    instrument = input("Enter 1 for PIANO, 2 for GUITAR, or 3 for DRUMS: ")
    while instrument not in instrument_options:
        instrument = input("Please try again. Enter 1 for PIANO, 2 for GUITAR, or 3 for DRUMS: ")

    if instrument == "1":
        instrument = "Piano"
    elif instrument == "2":
        instrument = "Guitar"
    else:
        instrument = "Drums"
    print("Thanks for answering - next question!")
    # print(f"INTERNAL STATUS OF INSTRUMENT: {instrument}")

    # Question 4
    print('''

        Question 4: Do you typically follow trends or stray from the mainstream?
        
    ''')
    commonly_known_options = ["1", "2"]
    commonly_known = input("Enter 1 for TREND FOLLOWER or 2 for TREND SETTER: ")
    while commonly_known not in commonly_known_options:
        commonly_known = input("Please try again. Enter 1 for TREND FOLLOWER or 2 for TREND SETTER: ")

    if commonly_known == "1":
        commonly_known = "Yes"
    else:
        commonly_known = "No"
    print("Thanks for answering - that was the last question!")
    # print(f"INTERNAL STATUS OF COMMONLY KNOW: {commonly_known}")


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

            You got.... {genre.name}!!!!

        ''')
