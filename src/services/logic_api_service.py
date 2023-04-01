from entities.game_state import GameState

class LogicAPI():
    # This class is reponsible for the logic that sits between everything
    # It does at least the following:
    #   - takes in user guesses and handles the response
    #   - 

    def __init__(self) -> None:
        self._game_state = GameState()

    # temp function for testing, to be removed
    def set_solution(self, word: str):
        self._game_state._current_solution = list(word)

    # Meant for use of: input_user_guess()
    def _compare_user_guess_to_solution(self, guess: list) -> list:
    # Function takes in a user guess and returns a list containing symbols
    # resulting from comparing each letter in guess to solution.
    #   - X for correct letter in correct place: "green" letter
    #   - * for correct letter in wrong place : "yellow" letter
    #   - _ for incorrect letter: "dark" letter

        solution = self._game_state._current_solution
        
        # Find number of letters in solution in order to 
        # keep track of duplicates in next step.
        solution_letter_counts = {}
        for letter in solution:
            if letter not in solution_letter_counts:
                solution_letter_counts[letter] = 0
            solution_letter_counts[letter] += 1

        # The following is done in two passes as "green" letters need to be 
        # found first, as they take priority over "yellow" letters.
        
        comparison_results = [None] * 5

        # first pass to find "green" letters
        for i, letter in enumerate(guess):
            if letter == solution[i]:
                if solution_letter_counts[letter]:
                    solution_letter_counts[letter] -= 1
                comparison_results[i] = "X"
        
        # second pass to find "yellow" and "dark" letters
        for i, letter in enumerate(guess):
            if letter != solution[i] and letter in solution_letter_counts and solution_letter_counts[letter]:
                solution_letter_counts[letter] -= 1
                result = "*"
            else:
                result = "_"

            if not comparison_results[i]:
                comparison_results[i] = result
            
        return comparison_results


    # this function is called by UI when inputting user guesses
    def input_user_guess(self, user_guess: list) -> None:

        def guess_is_valid_word(guess: list) -> bool:
            # TODO:
            # - check if word in wordbank to see if word is valid guess
            # for now just returns True
            return True
        
        # guard clause: if word is invalid, give "invalid word to UI and return"
        if not guess_is_valid_word(user_guess):
            #TODO:
            # - invoke self._ui_response_handler to issue "invalid word" to UI
            return ("Invalid Word", [])
        
        # from here on user is guess assumed to be valid

        comparison = self._compare_user_guess_to_solution(user_guess)
        self._game_state.add_user_guess((user_guess, comparison))

        return user_guess, comparison

    def get_letter_state(self) -> dict:
        return self._game_state._letter_state



logic_api_service = LogicAPI()