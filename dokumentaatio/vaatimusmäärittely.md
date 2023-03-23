# Software requirements specification

### Purpose of the application

The application is a clone of the popular game Wordle. In Wordle the player has to guess a predetermined five letter word. The player gives five letter words as input and is shown which, if any of the letters in their guess are correct. Using the process of elimination, the player has to work out the correct word in six guesses. 

### Users

The intial plan doesn't including implementation of users, as it is not necessary for this kind of application. Users could be implemented, if there is sufficient time at the end of the project and the application is otherwise feature complete. Implementing users would allow for personalised statistics, but is not in the intial scope.

### User interface

The application opens to the main game windowd. This is the only windows in the applicationn and the "how to play", "settings" and "statistics" buttons open up a modal. If a modal is open the rest of the main window is darkened to help readability. The statistics" modal also opens when the game ends.

### Functionality

* The application saves the state of an ongoing game and opens to that state
* The user can guess words by writing a valid five letter word and pressing enter
* Upon a valid word input, the application highlights letters followingly:
    * Incorrect letters: gray
    * Correct letters in the wrong place: yellow
    * Correcr letters in the right place: green
* This highlighting is also appllied to the "keyboard" section
* The "how to play" button to open a modal with instructions
* The "statistics" button opens a modal with statistics about previous games
* The "restart" button can be pressed after the game has ended, which resets the game with a new word
* The game is automatially reset every 24 hours
* Within the "options" modal:
    * An option for dark mode

