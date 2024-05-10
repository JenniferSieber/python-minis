"""
      Turtle Racing 
        - Graphical Python Racing with .turtle()
        - User selects number of Turtles
        - randomly generate different colored Turtles to race 
        - return results of race and time elapsed
        - inquire if want to race again
"""

import turtle
import time
import random
import time

WIDTH, HEIGHT = 700, 700
COLORS = ['lightblue', 'chartreuse', 'lightseagreen', 'green', 'lightcoral', 'yellow', 'lightgreen', 'lightsalmon', 'cyan', 'goldenrod']


def get_number_of_racers() :
    racers = 0
    while True :
        print('How many racers do you want for this race?')
        num_racers = input('Enter number between 2 - 10:  ')
        if num_racers.isdigit() :
            racers = int(num_racers)
            print(f'Number of racers: {racers}')
            print()
        else :
            print('Requires numeric input, try again. \n')
            continue

        if 2 <= racers <= 10 :
            return racers
        else :
            print('Number is not in the range 2 - 10. Try again. \n')


def race(colors) :
    turtles = create_turtles(colors)
    while True :
        for racer in turtles :
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10 :
                return colors[turtles.index(racer)], turtles.index(racer) + 1
    

def create_turtles(colors) :
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors) :
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.shapesize(3, 2)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_turtle() :
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)  
    screen.title(' 🐢 🐢 🐢 🐢 🐢  TURTLE RACING  🐢 🐢 🐢 🐢 🐢 ')
    screen.bgcolor('black')


def start_race(s) :
    print()
    print(s)
    print('____________________________ \n')
    answer = input('START press `S` (`q` to quit)  ').lower()
    print()
    if answer == 's' :
        racers = get_number_of_racers()
        init_turtle()
        random.shuffle(COLORS)
        colors = COLORS[:racers]
        start_time = time.time()
        winner_color, num = race(colors)
        end_time = time.time()
        time_elapsed = round(end_time - start_time)  
        print(f' 🐢🐢🐢  Winner of the Race in {time_elapsed} seconds: TURTLE #{num} in {winner_color.upper()}  🐢🐢🐢 \n')

        print()
        time.sleep(3)
        turtle.Screen().clear()
        turtle.Screen().bgcolor('black')  
        print('Do you want to do another Turtle Race? ')
        race_again = input('Start racing again? Enter `y` (or `q` to quit) ').lower() 
        
        if race_again == 'y' :
            print()
            start_race('  🐢 Turtle Race Again! 🐢  ')
        else :
            print()
            print('Thank you for visiting Turtle Racing. \n')
            change_mind = input('IF you want to START a Race: press `y`  ').lower()
            if change_mind == 'y' :
                start_race(' 🐢 Turtle Race Again 🐢  ') 
            else :
                print('Thank you for visiting Turtle Racing. \n')
                quit()
    else :
        print('Thank you for visiting Turtle Racing. \n')
        change_mind = input('IF you want to START a Race: press `y`  ').lower()
        if change_mind == 'y' :
            start_race(' 🐢 Turtle Race Again 🐢  ') 
        else :
            print('Thank you for visiting Turtle Racing. \n')
            quit()

start_race('🐢 🐢 WELCOME to the TURTLE RACES 🐢 🐢 ')
