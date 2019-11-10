#!/usr/bin/python3

import sys
import enum

def print_prompt():
    print("db > ")


def main(line=None):
  while True:
    print_prompt()
    user_input = line or input()
    if user_input == ".exit":
      break

    else:
      print("Unrecognized command '{}'.\n".format(user_input))



if __name__ == "__main__":
    if sys.stdin.isatty():
        main()
    else:
        for line in sys.stdin:
            main(line)