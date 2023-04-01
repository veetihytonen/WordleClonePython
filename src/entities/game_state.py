from string import ascii_lowercase

class GameState():
    # This class stores:
    #   - the current solution
    #     (fetched from DB before creation)
    #   - user guesses in the ongoing game 
    #     (fetched from DB before creation, updated as the user inputs words)
    #   - letter state: highest level of match found for each letter ie.
    #     which letters have been found "dark", "yellow" and "green"
    #     (built from user guesses on creations and updated angloside it)

    def __init__(self, current_solution: list, user_guesses: list) -> None:
        self._current_solution = current_solution
        self._user_guesses = user_guesses
    # - "current_solution" is the correct answer as a list of letters
    # - "user_guesses" is a list of tuples, where each tuple consists of:
    #   Item 0: guess recieved from UI, as a list of letters
    #   Item 1: results of comparing it to current_solution, as a list of symbols

        self._letter_state = {letter: "N" for letter in ascii_lowercase}
        for guess in user_guesses:
            self._update_letter_state(guess)
        
        # _letter_state has all letters in alphabet as keys and 
        # each has one of four symbols as value. Symbols are:
        #  "N" for   "grey": letter hasn't been guessed
        #  "_" for   "dark": letter has been guessed: 
        #                       - is not in current_solution
        #  "*" for "yellow": letter has been guessed: 
        #                       - is in current_solution
        #                       - is in wrong position in the guesses it appeared in
        #  "X" for  "green": letter has been guessed:
        #                       - is in current_solution
        #                       - is in the right position in a guess it appeared in

    def _update_letter_state(self, guess_data: tuple) -> None:
        
        def convert_symbol_to_num(symbol: str) -> int:
            if symbol == "N":
                return 0
            elif symbol == "_":
                return 1
            elif symbol == "*":
                return 2
            else:
                return 3

        word, comparison = guess_data
        for i, letter in enumerate(word):
            letter_state_curr = convert_symbol_to_num(self._letter_state[letter])
            if convert_symbol_to_num(comparison[i]) > letter_state_curr:
                self._letter_state[letter] = comparison[i]
    

    def add_user_guess(self, user_guess: tuple) -> None:
        self._user_guesses.append(user_guess)
        self._update_letter_state(user_guess)
    


