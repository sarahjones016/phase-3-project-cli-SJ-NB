from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import Fan, Review, Genre


if __name__ == '__main__':
   engine = create_engine('sqlite:///genre_app.db')
   Session = sessionmaker(bind=engine)
   session = Session()


   session.query(Fan).delete()
   session.query(Genre).delete()
   session.query(Review).delete()


   fake = Faker()


   # Genre Table
   genres = []
   showtunes = Genre(name="Showtunes", avg_bpm=117, style="Instrumental", prodominent_instrument="Piano", commonly_known="Yes")
   glam_rock = Genre(name="Glam Rock ", avg_bpm=125, style="Instrumental", prodominent_instrument="Piano", commonly_known="No")
   k_pop = Genre(name="K-pop", avg_bpm=175, style="Instrumental", prodominent_instrument="Guitar", commonly_known="Yes")
   punk_jazz = Genre(name="Punk Jazz", avg_bpm=125, style="Instrumental", prodominent_instrument="Guitar", commonly_known="No")
   swing = Genre(name="Swing", avg_bpm=132, style="Instrumental", prodominent_instrument="Drums", commonly_known="Yes")
   ska = Genre(name="Ska", avg_bpm=216, style="Instrumental", prodominent_instrument="Drums", commonly_known="No")
   jungle = Genre(name="Jungle", avg_bpm=160, style="Electronic", prodominent_instrument="Piano", commonly_known="Yes")
   psychedelic_trance = Genre(name="Psychedelic Trance", avg_bpm=140, style="Electronic", prodominent_instrument="Piano", commonly_known="No")
   disco = Genre(name="Disco", avg_bpm=120, style="Electronic", prodominent_instrument="Guitar", commonly_known="Yes")
   acid_breaks = Genre(name="Acid Breaks", avg_bpm=135, style="Electronic", prodominent_instrument="Guitar", commonly_known="No")
   house = Genre(name="House", avg_bpm=135, style="Electronic", prodominent_instrument="Drums", commonly_known="Yes")
   uplifting_trance = Genre(name="Uplifting Trace", avg_bpm=136, style="Electronic", prodominent_instrument="Drums", commonly_known="No")
   r_and_b = Genre(name="R&B", avg_bpm=70, style="Instrumental", prodominent_instrument="Piano", commonly_known="Yes")
   waltz = Genre(name="Waltz", avg_bpm=87, style="Instrumental", prodominent_instrument="Piano", commonly_known="No")
   reggae = Genre(name="Reggae", avg_bpm=75, style="Instrumental", prodominent_instrument="Guitar", commonly_known="Yes")
   bluegrass = Genre(name="Bluegrass", avg_bpm=95, style="Instrumental", prodominent_instrument="Guitar", commonly_known="No")
   blues = Genre(name="Blues", avg_bpm=70, style="Instrumental", prodominent_instrument="Drums", commonly_known="Yes")
   smooth_jazz = Genre(name="Smooth Jazz", avg_bpm=101, style="Instrumental", prodominent_instrument="Drums", commonly_known="No")
   hip_hop = Genre(name="Hip Hop", avg_bpm=90, style="Electronic", prodominent_instrument="Piano", commonly_known="Yes")
   ambient_music = Genre(name="Ambient Music", avg_bpm=65, style="Electronic", prodominent_instrument="Piano", commonly_known="No")
   lofi_hip_hop = Genre(name="Lofi Hip Hop", avg_bpm=75, style="Electronic", prodominent_instrument="Guitar", commonly_known="Yes")
   glitch_hop = Genre(name="Glitch-hop", avg_bpm=100, style="Electronic", prodominent_instrument="Guitar", commonly_known="No")
   dubstep = Genre(name="Dubstep", avg_bpm=85, style="Electronic", prodominent_instrument="Drums", commonly_known="Yes")
   downtempo = Genre(name="Downtempo", avg_bpm=85, style="Electronic", prodominent_instrument="Drums", commonly_known="No")

   session.add(showtunes)
   session.add(glam_rock)
   session.add(k_pop)
   session.add(punk_jazz)
   session.add(swing)
   session.add(ska)
   session.add(jungle)
   session.add(psychedelic_trance)
   session.add(disco)
   session.add(acid_breaks)
   session.add(house)
   session.add(uplifting_trance)
   session.add(r_and_b)
   session.add(waltz)
   session.add(reggae)
   session.add(bluegrass)
   session.add(blues)
   session.add(smooth_jazz)
   session.add(hip_hop)
   session.add(ambient_music)
   session.add(lofi_hip_hop)
   session.add(glitch_hop)
   session.add(dubstep)
   session.add(downtempo)

   session.commit()

   genres.append(showtunes)
   genres.append(glam_rock)
   genres.append(k_pop)
   genres.append(punk_jazz)
   genres.append(swing)
   genres.append(ska)
   genres.append(jungle)
   genres.append(psychedelic_trance)
   genres.append(disco)
   genres.append(acid_breaks)
   genres.append(house)
   genres.append(uplifting_trance)
   genres.append(r_and_b)
   genres.append(waltz)
   genres.append(reggae)
   genres.append(bluegrass)
   genres.append(blues)
   genres.append(smooth_jazz)
   genres.append(hip_hop)
   genres.append(ambient_music)
   genres.append(lofi_hip_hop)
   genres.append(glitch_hop)
   genres.append(dubstep)
   genres.append(downtempo)

   # Fan Table
   fans = []
   for i in range(12):
       fan = Fan(
           first_name=fake.first_name(),
           last_name=fake.last_name()
       )
       session.add(fan)
       session.commit()
       fans.append(fan)
  
   # Review Table
   reviews = []
   for fan in fans:
       for i in range(3):
        # create reviews that are associated with fans AND ALSO genres
        review = Review(
           star_rating=random.randint(1, 5),
           fan_id=fan.id,
           genre_id=random.choice(genres).id
        )
        reviews.append(review)
        session.add(review)
           

   session.commit()
   session.close()
