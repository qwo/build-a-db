#!/usr/bin/python3

import sys

from enum import Enum

class MetaCommandResult (Enum):
  META_COMMAND_SUCCESS = "META_COMMAND_SUCCESS"
  META_COMMAND_UNRECOGNIZED_COMMAND = "META_COMMAND_UNRECOGNIZED_COMMAND"

class PrepareResult (Enum):
  PREPARE_SUCCESS = "PREPARE_SUCCESS"
  PREPARE_UNRECOGNIZED_STATEMENT = "PREPARE_UNRECOGNIZED_STATEMENT"
  
class Statement (Enum):pass
class StatementType (Statement):
  STATEMENT_INSERT = "STATEMENT_INSERT"
  STATEMENT_SELECT = "STATEMENT_SELECT"
  

def do_meta_command(line):
  """
  @returns 0 or {MetaCommandResult}
  """
  if line == ".exit":
    return 0
  else:
    return MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND

def prepare_statement(line):
  """
  @returns ( {PrepareResult}, {STATEMENT_TYPE} )
  """
  if line == "insert":
    STATEMENT_TYPE = "STATEMENT_INSERT"
    return "PREPARE_SUCCESS", STATEMENT_TYPE
  elif line == "select":
    STATEMENT_TYPE = "STATEMENT_SELECT"
    return "PREPARE_SUCCESS", STATEMENT_TYPE
  else:
    return "PREPARE_UNRECOGNIZED_STATEMENT", None


def execute_statement(line):
  """
  @returns {PrepareResult} 
  or PREPARE_UNRECOGNIZED_STATEMENT
  """
  if line == "STATEMENT_INSERT":
    print("This is  where we would do an insert.\n")    
  elif line == "STATEMENT_SELECT":
    print("This is where we would do a select.\n")


def print_prompt():
    print("db > ")


def main(line=None):
  while True:
    print_prompt()
    user_input = line or input()
    if user_input == ".exit":
      break

    ## MetaCommand
    if user_input[0] == '.':
      meta_command = do_meta_command(user_input)
     # @TODO STATEMENT DETECT_TYPE META_COMMAND_SUCCESS ENUM AND PICK COMMAND
      if meta_command == "META_COMMAND_SUCCESS":
         pass
      elif meta_command == MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND:
        print("Unrecognized command '{}'.\n".format(user_input))
      continue # EXIT META COMMAND

    ## Statement
    prepare_status, statement = prepare_statement(user_input)
    
    # @TODO STATEMENT DETECT_TYPE PREPARE_SUCCESS ENUM AND PICK STATEMENT
    if prepare_status == PrepareResult.PREPARE_SUCCESS:
      continue
    elif prepare_status == PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT:
      print("Unrecognized keyword at start of '{}'.\n".format(user_input))
    execute_statement(statement)
    print("Executed.\n")



if __name__ == "__main__":
    if sys.stdin.isatty():
        main()
    else:
        for line in sys.stdin:
            main(line)