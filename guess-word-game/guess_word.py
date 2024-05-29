"""
        Guess the Word Game
            Player has 10 chances to guess the correct letters 
            and complete the hidden word.
            Keeps scores for player and computer.
            Tracks number of games played.
            Option to clear all scores and restart game.
            and normal options to replay game with existing scores.
            word list for randomize word option: 309 words.
"""
import string
import random
import os

word_list = [
            "tree", "flower", "mountain", "river", "lake", "ocean", "beach", "sunday", "language", "sun", "moon", "star", "cloud", "rain", "snow", "wind",
        "storm", "autumn", "swampland", "suitcase", "forest", "field", "desert", "canyon", "island", "volcano", "earthquake", "forest", "purse", 
        "tornado", "hurricane", "drought", "flood", "thunderstorm", "wildfire", "clock", "season", "avalanche", "glacier", "waterfall", "rainbow",
        "cave", "spring", "snowstorm", "people", "car", "bus", "train", "bicycle", "motorcycle", "plane", "boat", "winter", "course", "popcorn", 
        "subway", "taxi", "truck", "scooter", "helicopter", "rocket", "summer", "weekend", "coast", "apple", "banana", "carrot", "broccoli", 
        "cheese", "bread", "pasta", "rainshower", "trail", "rice", "pizza", "burger", "sandwich", "salad", "soup", "cake", "cookie", "weekday", 
        "granola", "chocolate", "ice cream", "smoothie", "coffee", "juice", "water", "saturday", "scripture", "ocean", "sea", "wave", "surf", 
        "tide", "whale", "dolphin", "shark", "rainbow", "sailboat", "fish", "coral", "reef", "shell", "starfish", "seagull", "lighthouse", 
        "sunset", "aliens", "buoy", "pier", "anchor", "whale", "submarine", "crab", "lobster", "sunrise", "console", "train", "track", "station", 
        "passenger", "engine", "conductor", "ticket", "afternoon", "fireplace", "platform", "schedule", "delay", "baggage", "signal", "rail", 
        "junction", "evening", "restaurant", "bridge", "tunnel", "commute", "transport", "public", "express", "freight", "morning", "sweatshirt", 
        "container", "cargo", "railroad", "crossing", "tablet", "paraglider", "mountain", "slacks", "escalator", "farm", "railway", "transit", 
        "tram", "locomotive", "caboose", "money", "sweater", "coupler", "switch", "turntable", "yard", "telegraph", "martini", "champagne", 
        "shirt","receipt", "highway", "railroad", "timetable", "wheel", "trolley", "volcano", "church", "trunk", "turbine", "temperature", 
        "underground", "underpass", "uniform", "united", "fishingpole", "upgrade", "upright", "vacation", "van", "juice", "vapor", "vaporize", 
        "synagogue", "heart", "velocity", "vent", "veranda", "vertical", "very", "vessel", "view", "cellphone", "dancer", "violet", "voice", 
        "volcano", "volume", "voyage", "wafer", "wagon", "computer", "garden", "wait", "walk", "warehouse", "warm", "wash", "waste", "desert", 
        "glacier", "witness", "water", "wave", "wax", "weather", "week", "weigh", "island", "paradise", "university", "south", "west", "wheel", 
        "north", "dresser", "while", "whip", "brush", "comb", "runner", "white", "who", "why", "wide", "wife", "will", "wind", "number", "college", "tuesday", "window", "wine", "wing", "winter", "wire", "wise", "wish", "racecar", "missionary", "saturn", "without", "woman", "wonder", "wood", "word", "work", "racetrack", "internet", "world", "worry", "worth", "would", "write", "wrong", "year", "trailer", "vacation", "yellow", "yes", "yesterday", "yet", "young", "chair", "table", "hospital", "movies", "zero", "zone", "zoo", "cabinet", "closet", "bedroom", "doorknob", "stockings", "zeppelin", "piano", "guitar", "trumpet", "heaven", "venus", "jupiter", "neptune", "breeze", "pluto", "rocket", "spaceship", "satellite"
]

letters = string.ascii_lowercase
game_count = 0
player_wins = 0
computer_wins = 0
words_used = []

print('\n👾 Guess the Word Game 👾\n'.upper())
print('The rules: You win if you can guess the word within 10 guesses! One Letter per guess.\n')
print(f'Games Played: {game_count} \n')

""" Clear terminal for new game """
def clear_terminal():
    # Check the platform and execute the corresponding command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems
        os.system('clear')

""" Get randomized word by index of word list """
def get_random_word(words) : 
    random_index = random.randint(0, len(word_list) - 1)
    word_to_play = word_list[random_index]
    words_used.append(word_to_play)
    return word_to_play

""" Set up and hide random word """
def setup_game() :
    word = get_random_word(word_list)
    hidden = []
    for i in word :
        hidden.append(' 👾 ')
    return word, hidden

""" Start the game or close out the game """
def start_game() :
    global player_wins
    global computer_wins
    global words_used 
    global game_count
    play = input('Would you like to start a game? (Y/N) ').lower()
    if play == 'y' :
        game_count += 1
        clear_terminal()
        print('\n👾 Guess the Word Game 👾\n'.upper())
        print("\nLet's Play!")
        print(f'\nGame: {game_count}') 
        print(f'Player wins: {player_wins}   Computer wins: {computer_wins}\n') 
        play_game()
    elif play == 'n' :
        reset_scores = input('\nDo you want to reset scores? (Y/N) ').lower()
        if reset_scores == 'y' :
            print('Scores and Game Reset!')
            clear_terminal()
            player_wins = 0
            computer_wins = 0
            game_count = 0
            words_used = []
            start_game()
        else :
            print('\n👾 Thank you for playing `Guess The Word` 👾\n')
            clear_terminal()
            start_game()           
    else :
        print('\n👾 Thank you for playing `Guess The Word`! Good bye! 👾\n')
        clear_terminal()
        start_game()

""" Update scores for player and computer """
def score(player=False, computer=False) : 
    global player_wins
    global computer_wins
    if player == True : 
        player_wins += 1
        player = False
    elif computer == True :
        computer_wins += 1
        computer = False
    return player_wins, computer_wins

""" With every valid guess - check if win condition """
def check_win(word, hidden) :
    if ' 👾 ' not in hidden :
        print('You have won!')
        p_score, c_score = score(True, False)
        print(''.join(hidden))
        print(f'\n Player Wins: {p_score}   Computer Wins: {c_score} \n')
        start_game()
        return True
    
""" Validate player guess  """
def validate_guess(guess, word) :
    if guess in letters :
        if guess in word :
            return True
        else :
            return False
    else :
        print(f'Guess of `{guess}` is not a letter.')    
        return False

""" Play the game """
def play_game() :
    word, hidden = setup_game()
    words_used.append(word)
    chars_guessed = []
    correct_chars = []
    correct = 0
    # print('Word to Guess: \n', word) Testing only
    print('Word to Guess: ')
    print(''.join(hidden))
    for i in range(10) :
        print(f'\nTurn {i + 1}')
        guess = input('Guess a single letter:  ').lower()
        print(f'You Guessed: `{guess.upper()}`')
        if guess in chars_guessed :
            print(f"You've already guessed `{guess.upper()}`.")
        chars_guessed.append(guess)
        guess_valid = validate_guess(guess, word)
        if guess_valid :
            # print(guess_valid)
            for i, char in enumerate(word) :
                if guess == char : 
                    hidden[i] = f' {char.upper()} '
                    correct_chars.append(char)
                    correct += 1
                    if correct == len(word) :
                        check_win(word, hidden)
        print('')
        print(''.join(hidden))
        print('')
    p_score, c_score = score(False, True)
    print(f'\nYou lost this round! The word was `{word.upper()}`\n')
    print(f'Player Wins: {p_score}   Computer Wins: {c_score}')
    start_game()

start_game()
