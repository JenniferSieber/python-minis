"""
    Typing Test with WPM score
        using curses in Python
        and a text file with lines of text to type
        provided randomly to the user.
"""
import curses
from curses import wrapper 
import time 
import random

def start_screen(stdscr) :
    stdscr.clear() 
    stdscr.addstr('Get your Words Per Minute Typing score!\n')
    stdscr.addstr('\nPress any key to begin! ')
    stdscr.refresh() 
    stdscr.getch()

def display_text(stdscr, target, current, wpm=0) :
    stdscr.addstr(target)
    stdscr.addstr(1, 0, F'WPM Score: {wpm}')

    for i,char in enumerate(current) :
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char :
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def load_target_line() :
    with open('text.txt', 'r') as f :
        lines = f.readlines()
        return random.choice(lines).strip() 
    
def wpm_test(stdscr) :
    target = load_target_line()
    current_chars = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True :
        time_elapsed = max(time.time() - start_time, 1)
        # wpm = round((len(current_chars) / (time_elapsed / 60)) / 5)
        wpm = round((len(''.join(current_chars).split()) / (time_elapsed / 60)))
        stdscr.clear()
        display_text(stdscr, target, current_chars, wpm)
        stdscr.refresh()

        if ''.join(current_chars) == target :   
            stdscr.nodelay(False) 
            break
        try :
            key = stdscr.getkey()
        except :
            continue
        if ord(key) == 27 :
            break

        BACKSPACE_KEYS = {'KEY_BACKSPACE', '\b', '\x7f', '\x08'}
        if key in BACKSPACE_KEYS :
            if len(current_chars) > 0 :
                current_chars.pop()       
        elif len(current_chars) < len(target) :
            current_chars.append(key)    

def main(stdscr) :
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True :
        wpm_test(stdscr)
        stdscr.addstr(2, 0, 'You typing test is completed! Press any key to continue (`ESC` to quit)')
        key = stdscr.getkey()

        if ord(key) == 27 :
            break

wrapper(main)
