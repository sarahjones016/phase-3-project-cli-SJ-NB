# Music Genre Quiz 

## Project Description
Are you in the mood for a new music genre but don't know where to start? We got you covered. Take this four question quiz and see what genre you should explore next!

## Demo

## Getting Started

This CLI application makes use of SQLAlchemy, Alembic, Python fundamentals, and Playsound. It can be executed via command line with

```shell
 python lib/cli.py
```

The 3 tables in the database (genre_app.db) can be seeded using the following command: 

````shell
python lib/db/seed.py
````

Playsound should be installed using the following command: 

````shell
pip install playsound
````

 If you are using a Mac and receive an error about a missing AppKit package, run the following command toform a bridge between Python and Objective-C on your Mac. : 
 
 ```shell
 pip3 install PyObjC.
```

### Set Up

This project utilizes three SQLAlchemy tables ("fans", "genres", and "reviews") that live within the genre_app database. The "fans" and "reviews" tables have been seeded with Faker data, while the "genres" table has been seeded manually with specific data that was collected for this project.

***

## The Build


### New Fan

When a user runs the CLI application, they are first welcomed. They are then prompted to enter their first and last name. After doing so, the "fans" table is updated with this new fan instance.

### Quiz

The user then begins the 4 question quiz. The "genres" table includes a single, unique genre for the 24 different answer combinations that a user can provide. The 4 question quiz also includes validation for each question. This ensures that the user gives an answer (an input) that our application is looking to accept. Once the user has completed the quiz, the application queries and filters the data in the "genres" table. Based on the 4 input values the user provides, the application returns a single genre recommendation. When the genre recommendation is provided, a 10 second audio clip associated with that genre is played (using Playsound).

### Review

After the user receives their genre recommendation and hears its audio clip, the user is then prompted to give the genre recommendation a review (1 - 5 star rating). Doing so updates the "reviews" table with a new review instance, by tying the user and genre together ("reviews" is a join table). Once the new review instance has been created, the application queries and filters the reviews. This allows for the application to provide the user with the average rating that their genre has received (from all reviews of that genre living in the database).

### Conclusion

Lastly, the user is then prompted to "play again" (rerun the game loop) or "quit" (break the game loop).

***

