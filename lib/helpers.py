from playsound import playsound

from db.models import Genre, Fan, Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///genre_app.db')
session = sessionmaker(bind=engine)()

# Colors
class Colors:
    bold = '\033[01m'
    underline = '\033[04m'

    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    blueishpurple = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

    class bg: #background
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


# Create a new fan instance, for the person using our CLI application
def create_fan():
    print(Colors.cyan, '''

    Let's get started!''')
    first_name = input('''
    Enter your first name: ''')
    last_name = input('''
    Enter your last name: ''')
    global new_fan
    new_fan = Fan(first_name=first_name, last_name=last_name)
    session.add(new_fan)
    print(f'''
    
    Hey {new_fan.first_name} {new_fan.last_name}! We'll ask you some quick questions to help you find a new music genre.
    ''')
    session.commit()

# Run the 4 question quiz that the user interacts with
def assign_genre():
    # QUESTION 1
    print(Colors.pink, '''

        Question 1: Do you prefer to listen to music while you chill or while you dance?

    ''')
    speed_options = ["1", "2"]
    speed = input('''
        Enter 1 for CHILL or 2 for DANCE: ''')
    while speed not in speed_options:
        speed = input('''
        Please try again. Enter 1 for CHILL or 2 for DANCE: ''')

    if speed == "1":
        speed = 0
    else:
        speed = 106
    print('''
        Thanks for answering - next question!
        ''')

    # QUESTION 2
    print(Colors.cyan,'''

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
    print(Colors.pink,'''

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
    print(Colors.cyan,'''

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
        global genres
        genres = session.query(Genre).filter(
            (style == Genre.style), (Genre.avg_bpm < 106), (instrument == Genre.prodominent_instrument), (commonly_known == Genre.commonly_known)
        )
    else:
        genres = session.query(Genre).filter(
            (style == Genre.style), (Genre.avg_bpm >= 106), (instrument == Genre.prodominent_instrument), (commonly_known == Genre.commonly_known)
        )

    for genre in genres:
        print(Colors.pink,f'''

        You should listen to more.... {genre.name} music!!!!                                                                       

   ,φ▒╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▒╗    
  ╒╬╬╬▓▓▓▓▒╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╠╠╠╬╬╬╬╬╬╬╠╠╩╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬ε  
  ╠╠╣██▀╙██▒╬╬╬╬╬╬╬╬╬╬╝╬╫╣▓▓██████████████▓▓╫╬╬╝╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╠╠╠╬╬╬╬╡  
  ╠╠╬██████╬╬╬╬╬╬╬╬╬╫▓▓████████████████████████▓▓╫╬╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▒╠╠╠╠╠╬╬╡  
  ╠╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████████████████████████████████▓▀╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╠▒╠╠╠╠╬╬╬╡  
  ╠╠╬╬╬╬╬╬╬╬╬╬╣▓██████████████████████████████████████▓╬╠╬╬╬╬╬╬╬▓▓▀▀▀░▄▒╬╬╬╬╬╡  
  ╠╠╬╬╬╬╬╬╬╬╫▓██████████████████████████████████████████▓╬╬╬╬╬╣█▒╩░╓░╚░▓▌╬╬╬╬╡  
  ╠╠╬╬╬╬╬╬╬▓▓█████████████████████████████████████████████▓╠╠╬╫▌╠░╚╠╠ ╠╣█╬╬╬╬╡  
  ╠╠╬╬╬╬╬╢▓████████████████████████████████████████████████▓╬╬╬█▌╠╦╔φ╠╬█▒╬╬╬╬╡  
  ╠╠╬╬╬╬╢▓██████████████████████████████████████████████████▓╬╬╠░╠╫▓▓▓╬╬╬╬╬╬╬╡  
  ╠╠╬╬╬╣▓████████████████████████▀▀▀▓████████████████████████╣▒')╠╬╬╬╬╬╬╬╬╬╬╬╡  
  ╠╠╬╬╬▌█████████████████████╩▒╠╠╠╠╠╠╠╠╠╬█████████████████████.]╠╬╬╬╬╬╣╣╣╣╬╬╬╡  
  ╠╠╬╬╣╣███████████████████╬╠╠╠╠╠╠╠╠╠╠╠╠╠╠╬██████████████████▀.▒╬╬╬╬╬╬╬╣█╬╬╬╬╡  
  ╠╠╬╠╫▓██████████████████▒╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠▒╬████████████████▌.▓▌╬╬╬╬╬╬╬╣█╬╬╬╬╡  
  ╠╠╬╬╫███████████████████▒╠╠╠╠╠╠╠╫▌╠╠╠╠╠╠╠╠████████████████'▐█▌╠╬╬╬╬╬╬╣█╬╬╬╬╡  
  ╠╠╬╬▓███████████████████▒╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠╠███████████████▀ ██▌╬╬╬╬╬╬╬╣█╬╬╬╬╡  
  ╠╠╬╬╫╫██████████████████▓▒╠╠╠╠╠╠╠╠╠╠╠╠╠╠▒▓███████████████'╫█▌▌╬╬╬╬╬╬╬╣█╬╬╬╬╡  
  ╠╠╬╬▒▌████████████████████▄╬╠╠╠╠╠╠╠╠╠╩╠▄████████████████~▐██╣▒╬╬╬╬╬╬╬╬╬╬╬╬╬╡  
  ╠╠╬╬╬╫▓█████████████████████▓▄▄▒╠╠▒▄▄▓█████████████████▀.██▓▌╠╬╬╬╬╬╬╬╣█╬╬╬╬╡  
  ╠╠╬╬╬╬▓███████████████████████████████████████████████▀ ▓██▓╠╬╬╬╬╬╬╬╬╣█╬╬╬╬╡  
  ╠╠╬╬╬╬╠▓███████████████████████████████████████████▓╙,▄███▓╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╡  
  ╠╠╬╬╬╬╬╬▀▓████████████████████████████████████▀╠φ╠╚▄▓███▓▀╠╬╬╬╬╬╬╬╬╬╬╬▒╬╬╬╬╡
  ╠╠╬╬╬╬╬╬╠╬╬████████████████████████████████▀φ╠╠╠╠╠▓████▓╠╬╬╬╬╬╬╬╬╬╬╬╫░╠╣╬╬╬╡  
  ╠╠╬╬╬╬╬╬╬╬╠╬╬████████████████████████████'╚╠╠╩╙▄▓████▓╬╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬▒▒╬╬╬╡  
  ╠╠╬╬╬╬╬╬╬╬╬╬╠╬╫▓██████████████████████████⌂,▄▄▀███▓▌╠╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╫▒╬╟╬╬╬╡  
  ╠╠╬╬▓▀▀╣▒╬╬╬╬╬╠╬╬╣▓███████████████████████████▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╡  
  ╠╠╣▌╠╠╠╠╣▒╬╬╬╬╬╬╬╬╠╬╬╝████████████████████▓▓╝╬╬╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╟╬╬╫╬╬╬╡  
  ╚╬╬▓▒╠╠▒▓▒╬╬╬╬╬╬╬╬╬╬╬╬╬╠╬▒▒╬╫╝╫▓▓▓▓╫╝╫╬╬▒╬╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣╫╬╬╬╬▒  
   ╙╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╩   
        ''')

    # Play Audio
    genre_name = genre.name.lower().replace(" ", "_")
    playsound(f"lib/Audio/{genre_name}.mp3")

# Create a new review instance. This takes the new fan's id and the id of they genre they've be assigned
def create_review():
    print('''
    
    Time to review the genre you recieved!'''
        )
    star_options = ["1", "2", "3", "4", "5"]
    star = input('''
        Enter 1 - 5 to give the genre a star rating: ''')
    while star not in star_options:
        star = input('''
        Please try again. Enter 1, 2, 3, 4, or 5 to give the genre a star rating: ''')
    for genre in genres:
        new_review = Review(star_rating=star, fan_id=new_fan.id, genre_id=genre.id)
        session.add(new_review)
        print(f'''
                        
        Thanks for giving {genre.name} a {star} star review!
                    ''')
    session.commit()


# Pull the average star rating for the genre the new fan just reviewed
def average_review():
    for genre in genres:
        filtered_reviews = session.query(Review).filter(genre.id == Review.genre_id)
        filtered_ratings_list = []
        for review in filtered_reviews:
            filtered_ratings_list.append(review.star_rating)
        average = round(sum(filtered_ratings_list) / len(filtered_ratings_list), 2)
        print(f'''
        The average star rating for {genre.name} is {average}
        ''')



