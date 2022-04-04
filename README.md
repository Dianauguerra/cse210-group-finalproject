## Space Race
Space Race is a space-themed racing game where you race against your opponent in outer space. You race across the galaxy, dodging meteorits. Each successful trip through space earns an individual score.

## Rules
There are two players. Each one has a ship. The ships can move up to down or viceversa. To move, Player one uses "W" for UP and "S" for DOWN. Player two uses "I" for UP and "K" for DOWN. Whoever gets to the top succesfully by dodging the meteors, earns a point. The race lasts three minutes, good luck! To stop the game simply close the window.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Arcade Python 2.6.10 installed and running on your machine. You can install Arcade Python by opening a terminal and running the following command.
```
python3 -m pip install arcade
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 space_race
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    ( project root folder )
+-- space_race          ( source code for game )
  +-- game              ( game specific classes )
    +-- casting         ( various actor classes )
    +-- directing       ( game class ) 
    +-- shared          ( various shared clases )
  +-- __main__.py       ( program entry point )
  +-- constants.py      ( game constants )
+-- README.md           ( general info )
```

## Required Technologies
---
* Python 3.10.2
* Arcade Python 2.6.10

## Authors
---
* Miguel López ( lop18028@byui.edu ) : Create and code __main__.py, all the casting classes( Actor, Meteorite, Score, Spacecraft and Square_Timer classes ) and Game class from directing classes. Oversaw the review of the project as a whole.
* Ryan Weinheimer ( ryanweinheimer@gmail.com ) : Update Game class from directing classes. Create and code Point Class from shared clases and constants.py file. Checked that the program apply the four principles of programming with classes.
* Diana Guerra ( diana.1609@hotmail.com ) : Create the team repository and README file. Create and code Velocity Class from shared clases. Checked that the program apply the four principles of programming with classes.
* Eduardo Mosquera Galarza ( mos21008@byui.edu ) : Updated Score class from casting classes and updated Point class from shared classes.
* Chioneso Chatayika( cchatayika@outlook.com ) : Updated Velocity class from shared classes. Updated constants.py file.