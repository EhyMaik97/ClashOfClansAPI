"""
Clash of Clans API - main
"""
from utils.api_menus import (
    show_main_menu, 
    show_clans_menu, 
    show_goldpass_menu, 
    show_players_menu, 
    show_labels_menu,
    show_locations_menu,
    show_leagues_menu
)
from utils.method_menus import (
    manage_clans_chioice, 
    manage_goldpass_chioice, 
    manage_players_chioice, 
    manage_labels_chioice,
    manage_locations_chioice,
    manage_leagues_chioice
)

def main():
    while True:
        show_main_menu()
        choice = input("#> ")

        match choice:
            case '1':
                """Clans"""
                show_clans_menu()
                manage_clans_chioice(input("#> "))
            case '2':
                """E-Sports"""
                print("No Documentation for E-Sports API call")
            case '3':
                show_goldpass_menu()
                manage_goldpass_chioice(input("#> "))
            case '4':
                """Labels"""
                show_labels_menu()
                manage_labels_chioice(input("#> "))
            case '5':
                """Leagues"""
                show_leagues_menu()
                manage_leagues_chioice(input("#> "))
            case '6':
                """Locations"""
                show_locations_menu()
                manage_locations_chioice(input("#> "))
            case '7':
                """Players"""
                show_players_menu()
                manage_players_chioice(input("#> "))
            case '0':
                print("Exit.")
                break
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()