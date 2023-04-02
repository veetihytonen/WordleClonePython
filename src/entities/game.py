class Game:
    # An instance of Game represents state of one game of wordle
    def __init__(self, solution: str, user_guesses: list = []) -> None:
        # user_guesses formatting: [[{'char': 's', 'level': 1}...]...]

        # Resolution represents win / loss state:
        # If game is ongoing: None
        # If game ends in win: 1
        # If game ends in loss: 0

        self._resolution = None
        self._solution = list(solution)
        self._user_guesses = user_guesses
        self._guessed_letters_state = {}

        for guess in self._user_guesses:
            self._update_guessed_letters_state(guess)
    
    # temp function for testing, to be removed
    def set_solution(self, word):
        self._solution = list(word)


    def _update_guessed_letters_state(self, guess_data: list) -> None:
        for char_data in guess_data:
            char, level = char_data['char'], char_data['level']
            if char not in self._guessed_letters_state:
                self._guessed_letters_state[char] = level
                continue
            if level > self._guessed_letters_state[char]:
                self._guessed_letters_state[char] = level


    def _compare_guess_to_solution(self, guess: list) -> list:
        remaining_letters = self._solution[:]
        comparison_results = [None] * 5

        # remaining_letters is to keeps track of correct letters found in guess

        # comparison_results (return value) formatting: [{'char': s, 'level': 1}...] 
        # value of the key: 'level' signifies how well character in guess mathces solution:
        # - 0 for: character not in solution
        # - 1 for: character in solution at different index
        # - 2 for: character in solution at same index

        # The comparison is done in two passes as "green" letters need to be 
        # found first, as they take priority over "yellow" letters.
        
        # first pass to find "green" letters
        for i, letter in enumerate(guess):
            if letter == self._solution[i]:
                comparison_results[i] = {'char': letter, 'level': 2}
                remaining_letters[i] = None
        # second pass to assign "yellow" and "dark" letters
        for i, letter in enumerate(guess):
            if comparison_results[i]:
                continue
            if letter in remaining_letters:
                comparison_results[i] = {'char': letter, 'level': 1}
                j = remaining_letters.index(letter)
                remaining_letters[j] = None
            else:
                comparison_results[i] = {'char': letter, 'level': 0}
            
        return comparison_results
    
    def _guess_is_valid_word(self, guess: list) -> bool:
        # will check if guess in list of valid words
        # for now just returns True
        return True

    def input_guess(self, guess: list) -> None:
        if not self._guess_is_valid_word(guess):
            return "some error here"
        
        comparison_data = self._compare_guess_to_solution(guess)
        
        self._user_guesses.append(comparison_data)
        self._update_guessed_letters_state(comparison_data)


    

            


