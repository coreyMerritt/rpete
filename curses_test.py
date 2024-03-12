import keyboard
import curses

#Testing the curses library here to hide keypresses, we'll use this functionality in rpete soon.
stdscr = curses.initscr()
for x in range(20):
    keyboard.wait('a')
