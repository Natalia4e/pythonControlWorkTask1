import logger
import logging
import main

def menu():
    while True:
        type_num = input("Choise\n"
                         "1 - add_new_note\n"
                         "2 - change_note\n"
                         "3 - delete_note\n"
                         "4 - search_note\n"
                         "6 - show_all_notes\n"
                         "5 - exit\n")
        match type_num:
            case "1":
                main.add_new_note()
                pass
            case "2":
                main.change_note()
                pass
            case "3":
                main.delete_note()
                pass
            case "4":
                main.search_note()
                pass
            case "5":
                logging.info("Stop program")
            case "6":
                main.show_all_notes()
            case _:
                logging.error("ERR")
                print("ERR")


menu()