from ui import *

def run():

    apartments = [

        {"id": 1, "water": 100, "heat": 10, "elec": 0, "gas": 250, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 100, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 4, "water": 100, "heat": 100, "elec": 100, "gas": 100, "other": 100},
        {"id": 5, "water": 0, "heat": 200, "elec": 0, "gas": 0, "other": 400},
        {"id": 6, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 7, "water": 0, "heat": 200, "elec": 0, "gas": 0, "other": 0},
        {"id": 8, "water": 0, "heat": 245, "elec": 20, "gas": 234, "other": 0},
        {"id": 9, "water": 104, "heat": 0, "elec": 500, "gas": 0, "other": 0},
        {"id": 10,"water": 300, "heat": 0, "elec": 0, "gas": 400, "other": 0}

    ]

    undoList = []

    while True:
        command = input(">> ").split()
        c = command[0]
        if c == "add":
            ui_addExpense(apartments, undoList, command)
        elif c == "list":
           ui_print(apartments, command)
        elif c == "remove":
            ui_remove(apartments, undoList, command)
        elif c == "replace":
            ui_replace(apartments, undoList, command)
        elif c == "filter":
            ui_filter(apartments, undoList, command)
        elif c == "max":
            ui_max(apartments, command)
        elif c == "sort":
            ui_sort(apartments, command)
        elif c == "sum":
            ui_sum(apartments, command)
        elif c == "undo":
            ui_undo(apartments, undoList)
        elif c == "help":
            ui_help()
        elif c == "exit":
            return
        else:
            print("Invalid command!")


run_tests()
run()