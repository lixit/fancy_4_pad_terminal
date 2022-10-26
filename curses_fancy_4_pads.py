import curses
import time
import concurrent.futures
from threading import Lock
import random
from typing import List

mutex = Lock()


def print_hello(pad, yx: List, low_right: List):
    while True:
        try:
            pad.addstr("*** Hello World ***", curses.color_pair(1))
        except curses.error:
            pad.clear()
            pad.addstr(0, 0, "*** Hello World ***\n")
        with mutex:
            pad.refresh(0, 0, yx[0], yx[1], low_right[0], low_right[1])
        time.sleep(random.uniform(0.1, 0.3))


def draw_menu(stdscr):
    k = 0
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    pad_list = []
    height, width = stdscr.getmaxyx()

    # middle point of the window
    x_mid = int(0.5*width)
    y_mid = int(0.5*height)

    yx_list = [[0, 0], [0, x_mid], [y_mid, 0], [y_mid, x_mid]]
    lower_right_list = [[y_mid - 2, x_mid - 3], [y_mid - 2,
                                                 width-1], [height - 1, x_mid - 3], [height-1, width-1]]

    for i in range(4):
        pad_list.append(curses.newpad(y_mid, x_mid))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(print_hello, param1, param2, param3)
                   for param1, param2, param3 in zip(pad_list, yx_list, lower_right_list)]
        # return_values = [f.result() for f in futures]


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
