import curses
from curses import wrapper
import time
import random
import csv
import datetime

# Load text from a file
def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# Display text and typing progress
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

# Function to input username
def get_username(stdscr):
    stdscr.addstr(2, 0, "Enter your name: ")
    stdscr.refresh()
    
    username = []
    
    while True:
        stdscr.addstr(2, 18, "".join(username) + " ")  # Display typed username
        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 10:  # Enter key (ASCII 10)
            break
        elif key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(username) > 0:
                username.pop()
        elif len(username) < 20:  # Limit username length
            username.append(key)

    return "".join(username).strip()

# Typing test function
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    stdscr.clear()
    username = get_username(stdscr)  # Get and display username

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    time_taken = round(time.time() - start_time, 2)

    # Store result in CSV
    with open("typing_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, datetime.datetime.now(), wpm, time_taken])

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

    while True:
        wpm_test(stdscr)
        stdscr.addstr(3, 0, "Test Completed! Press any key to continue or ESC to exit.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
