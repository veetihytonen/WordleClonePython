from services.ui_command_handler_service import ui_command_handler_service

class LogicAPI():
    # This class is reponsible for the logic that sits between everyhting
    # It does at least the following:
    #   - takes in user guesses and handles the response
    #   - 

    def __init__(self) -> None:
        # this will be fetched from DB on program start / game restart
        self._current_correct_word = []

        # This object will be an interface for issuing commands to UI from Logic API.
        # Intended use is for issuing commands to UI when options / game state change,
        # not for normal word comparison.
        self._ui_command_handler = ui_command_handler_service

    @property
    def current_correct_word(self) -> list:
        return self._current_correct_word

    @current_correct_word.setter
    def current_correct_word(self, word_as_letters_in_list: list) -> None:
        self._current_correct_word = word_as_letters_in_list


    # Meant for use of: input_user_guess()
    def _compare_user_guess_to_correct_word(self, guess: list) -> list:
    # Function takes in user guess and outputs list of tuples. Tuples are composed of:
    # Item 0: corresponding letter in the user guess
    # Item 1: symbol for result of comparing that letter to correct word:
    #   - X for correct letter in correct place
    #   - * for correct letter in wrong place
    #   - _ for incorrect letter

        correct_word = self._current_correct_word
        word_comparison_results = [None] * 5

        correct_word_letter_counts = {}
        for letter in correct_word:
            if letter not in correct_word_letter_counts:
                correct_word_letter_counts[letter] = 0
            correct_word_letter_counts[letter] += 1

        # The following done in two passes as "green" letter need to be 
        # found first, as they take priority over "yellow" letters

        # first pass to find letters in correct place
        for i, letter in enumerate(guess):
            if letter == correct_word[i]:
                if correct_word_letter_counts[letter]:
                    correct_word_letter_counts[letter] -= 1
                word_comparison_results[i] = (letter, "X")
        
        # second pass to look for correct letters in wrong place / assign incorrect letters
        for i, letter in enumerate(guess):
            letter_comparison_result = [letter]
           
            if letter != correct_word[i] and letter in correct_word_letter_counts and correct_word_letter_counts[letter]:
                correct_word_letter_counts[letter] -= 1
                letter_comparison_result.append("*")
            else:
                letter_comparison_result.append("_")

            if not word_comparison_results[i]:
                word_comparison_results[i] = tuple(letter_comparison_result)
            
        return word_comparison_results


    def input_user_guess(self, user_guess: list) -> tuple:
    # this function is called by UI when inputting user guesses and returns tuple in which:
    #   - item 0: Error Code. If empty, no error occured
    #   - item 1: output of comparisons, can be empty if error occured

        def guess_is_valid_word(guess: list) -> bool:
            # TODO:
            # - check if word in wordbank to see if word is valid guess
            # for now just return True
            return True
        
        # guard clause: if word is invalid, give "invalid word to UI and return"
        if not guess_is_valid_word(user_guess):
            #TODO:
            # - invoke self._ui_response_handler to issue "invalid word" to UI
            return ("Invalid Word", [])
        
        # from here on user is guess assumed to be valid

        return self._compare_user_guess_to_correct_word(user_guess)



            
        

        







logic_api_service = LogicAPI()