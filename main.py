"""
Clash of Clans API - main
"""
import importlib.util
from api import clans, esports, goldpass, labels, leagues, locations, players
from utils.helpers import get_methods_from_module, show_methods_menu, show_menu


def main():
    while True:
        show_menu()
        choice = input("#> ")

        match choice:
            case '1':
                """Clans"""
                methods = get_methods_from_module("clans")
                show_methods_menu(methods)
                method_choice = input("Select a clans method: ")
                try:
                    selected_method = methods[int(method_choice) - 1]
                except (IndexError, ValueError):
                    print("Invalid choice.")
            case '2':
                """E-Sports"""
                return "No Documentation for E-Sports API call"
            case '3':
                """Goldpass"""
                return "Coming Soon"
            case '4':
                """Labels"""
                return "Coming Soon"
            case '5':
                """Leagues"""
                return "Coming Soon"
            case '6':
                """Locations"""
                return "Coming Soon"
            case '7':
                """Players"""
                pass
                # get_players_method()
            case '0':
                print("Exit.")
                break
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()