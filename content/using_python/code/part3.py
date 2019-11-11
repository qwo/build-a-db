#!/usr/bin/python3

import sys

from collections import namedtuple
from enum import Enum


class MetaCommandResult(Enum):
    META_COMMAND_SUCCESS = "META_COMMAND_SUCCESS"
    META_COMMAND_UNRECOGNIZED_COMMAND = "META_COMMAND_UNRECOGNIZED_COMMAND"


class PrepareResult(Enum):
    PREPARE_SUCCESS = "PREPARE_SUCCESS"
    PREPARE_SYNTAX_ERROR = "PREPARE_SYNTAX_ERROR"
    PREPARE_UNRECOGNIZED_STATEMENT = "PREPARE_UNRECOGNIZED_STATEMENT"

class ExecuteResult(Enum):
    EXECUTE_SUCCESS = "EXECUTE_SUCCESS"
    EXECUTE_TABLE_FULL = "EXECUTE_TABLE_FULL"

class Statement(Enum):
    pass


class StatementType(Statement):
    STATEMENT_INSERT = "STATEMENT_INSERT"
    STATEMENT_SELECT = "STATEMENT_SELECT"


CONST_MAX_PAGES = 1024
CONST_MAX_ROW_PER_PAGE = 4096

class Table():

    def __init__(self, ):
        self.table_name = "default table"
        self.pages = CONST_MAX_PAGES
        self.index = [[]*CONST_MAX_PAGES]
        self.num_rows = 0
        self.fields = ["id", "username", "email"]
        self.Row = namedtuple('Row', self.fields)

    def insert_row(self, row):
        page = 0
        self.index[page].append(        self.serialize_row(row))
        self.num_rows +=1
        return "inserted 1 in {}".format(self.table_name)
    
    def select(self, line):
        select = []
        for i in self.index:
            select.extend(i)
        return select

    def serialize_row(self, line):
        return self.Row._make(line.split(" ")[1:])


def do_meta_command(line):
    """
  @returns 0 or {MetaCommandResult}
  """
    if line == ".exit":
        exit(0)
    else:
        return MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND


def prepare_statement(line):
    """
  @returns ( {PrepareResult}, {STATEMENT_TYPE} )
  """
    if "insert" in line:
        STATEMENT_TYPE = StatementType.STATEMENT_INSERT
        input_buffer = line.split(" ")
        if len(input_buffer) != 4:
            return "PREPARE_SYNTAX_ERROR", None
        return "PREPARE_SUCCESS", STATEMENT_TYPE
    elif "select" in line:
        STATEMENT_TYPE = StatementType.STATEMENT_SELECT
        return "PREPARE_SUCCESS", STATEMENT_TYPE
    else:
        return "PREPARE_UNRECOGNIZED_STATEMENT", None


def execute_statement(statement, table, line):
    """
  @returns {PrepareResult} 
  or PREPARE_UNRECOGNIZED_STATEMENT
  """
    print(statement)
    if statement == StatementType.STATEMENT_INSERT:
        print("This is where we would do an insert.\n")
        
        return ExecuteResult.EXECUTE_SUCCESS,         execute_insert(line, table)
    elif statement == StatementType.STATEMENT_SELECT:
        print("This is where we would do a select.\n")
        return ExecuteResult.EXECUTE_SUCCESS,         execute_select(line, table)
    else:
        return None, None

def execute_insert(line, table):
    return table.insert_row(line)


def execute_select(line, table):
    return table.select(line)


def print_prompt():
    print("db > ")



table = Table()
def main(line=None):
    while True:
        print_prompt()
        user_input = line or input()
        user_input = user_input.strip()

        ## MetaCommand
        if user_input[0] == ".":
            meta_command = do_meta_command(user_input)
            # DETECT_TYPE META_COMMAND_SUCCESS ENUM AND PICK COMMAND
            if meta_command == "META_COMMAND_SUCCESS":
                pass
            elif meta_command == MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND:
                print("Unrecognized command '{}'.\n".format(user_input))
            continue  # EXIT META COMMAND

        ## Statement
        prepare_status, statement = prepare_statement(user_input)

        # STATEMENT DETECT_TYPE PREPARE_SUCCESS ENUM AND PICK STATEMENT
        if prepare_status == PrepareResult.PREPARE_SUCCESS:
            continue
        elif prepare_status == PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT:
            print("Unrecognized keyword at start of '{}'.\n".format(user_input))
        execute_status, results = execute_statement(statement, table, user_input)
        
        if execute_status == ExecuteResult.EXECUTE_SUCCESS:
            print('executed results:', results)
            print("Executed.\n");
        elif  execute_status == ExecuteResult.EXECUTE_TABLE_FULL:
            print("Error: Table full.\n");

        # Get around to break
        if line:
            break


if __name__ == "__main__":
    if sys.stdin.isatty():
        main()
    else:
        for line in sys.stdin:
            main(line)
