"""
      Randomized, Timed Math Quiz
        - user selects length of Quiz
        - randomly generate math questions
        - check answer, move on to next randomly generated math question,
          only after receiving correct response on current question.
            - keep track of number of incorrect responses
            - quiz is timed
"""
import random
import time
# write variables will use as constants and change through out the quiz

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 2
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10

# generate an individual expression 
def generate_problem() :
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + ' ' + operator + ' ' +  str(right) 
    answer = eval(expr)

    return expr, answer


# start the quiz process
def quiz_generation(greet_str = 'Welcome to the Math Quiz!') :
    print(greet_str)
    print('Enjoy this Randomized, Timed Math Quiz, Good Luck!')
    yes = input('Create your Randomized, Timed Math Quiz? (Press `y` for yes!):   ').lower()

    if yes == 'y' :
        print()
        print('Select how many expressions you want to complete: ')
        problem_ct = input('Enter the amount (numerically):  ')

        if problem_ct.isdigit():
            pct = int(problem_ct)
            print(f'Generating your Randomized Timed Math Quiz with {pct} expressions to solve. ')
            start_quiz(pct)
        else :
            print(f'Your response: ` {problem_ct} ` is invalid.')
            quiz_generation('Try to create a Randomized Timed Math Quiz -again.')
    else :
        print('Thank you for visiting the Randomized, Timed Math Quiz!')
        accident = input('Did you want to start a quiz? Enter `yes`:  ').lower()
        if accident == 'yes' :
            quiz_generation('Try to create a Randomized Timed Math Quiz -again.')

# start the quiz and quiz timer
def start_quiz(pct) :
    incorrect = 0
    print('Are you ready to start the quiz timer? ')
    print('Timer will `start` immediately after pressing Enter key.')
    timer_start = input('START? (press ENTER key)   ').lower()

    start_time = time.time()

    if not pct :
        pct = TOTAL_PROBLEMS
    for i in range(pct) :
        express, answer = generate_problem()

        while True :
            print()
            print('Problem #:  ', i + 1)
            # print(express, answer) testing
            print(f'Problem {i + 1}:    {express} = ')
            guess = input('Your Answer(numeric):  ')

            if guess == str(answer) :
                print('Correct')
                break
            print('Incorrect, try again: ')
            incorrect += 1

    end_time = time.time()
    time_elapsed = round(end_time - start_time)  
    print()
    print('Thank you for completing your Randomized, Timed Math Quiz! ')
    print(f'You solved {pct} expressions in {time_elapsed} seconds with {incorrect} incorrect responses. ')
    print()
    play_again = input('Do you want to do another quiz?  Press `y`:   ').lower()

    if play_again == 'y' :
        quiz_generation('Awesome!')
    else :
        print('Thank you for using the Randomized, Timed Math Quiz! Goodbye.')

quiz_generation()
