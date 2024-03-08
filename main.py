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

#Clan tag #2G9JQRUJR
#Palyer tag #2LYUJ82G9

def main():
    while True:
        show_main_menu()
        choice = input("#> ")

        match choice:
            case '1':
                """Clans"""
                show_clans_menu()
                method_clan_choice = input("#> ")
                manage_clans_chioice(method_clan_choice)
            case '2':
                """E-Sports"""
                return print("No Documentation for E-Sports API call")
            case '3':
                show_goldpass_menu()
                method_goldpass_choice = input("#> ")
                manage_goldpass_chioice(method_goldpass_choice)
            case '4':
                """Labels"""
                show_labels_menu()
                method_players_choice = input("#> ")
                manage_labels_chioice(method_players_choice)
            case '5':
                """Leagues"""
                show_leagues_menu()
                method_players_choice = input("#> ")
                manage_leagues_chioice(method_players_choice)
            case '6':
                """Locations"""
                show_locations_menu()
                method_locations_choice = input("#> ")
                manage_locations_chioice(method_locations_choice)
            case '7':
                """Players"""
                show_players_menu()
                method_players_choice = input("#> ")
                manage_players_chioice(method_players_choice)
            case '0':
                print("Exit.")
                break
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()