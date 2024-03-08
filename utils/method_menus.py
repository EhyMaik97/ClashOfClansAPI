"""
Calsh of Clans API - Methods menus
"""
from models.clans_filter import ClansFilter
from api import clans, goldpass, players, labels, locations, leagues
from utils.helpers import coc_tag_input


def manage_clans_chioice(chosen_method):
    """
    Clans methods menu
    """
    match chosen_method:
        case '1':
            print("Enter the clan tag")
            clan_tag = coc_tag_input(input("#> "))
            print(clans.get_clan_current_war_league_group(clan_tag))
        case '2':
            print("Enter the war tag")
            war_tag = coc_tag_input(input("#> "))
            print(clans.get_clan_war_leagues(war_tag))
        case '3':
            print("Enter the clan tag")
            clan_tag = coc_tag_input(input("#> "))
            print(clans.get_clan_warlog(clan_tag))
        case '4':
            print("Enter the clan name (or nothing)")
            clan_name = input("#> ")
            print("Enter the war frequency (or nothing)")
            war_frequency = input("#> ")
            print("Enter the location id (or nothing)")
            location_id = input("#> ")
            print("Enter the number of min members (or nothing)")
            min_members = input("#> ")
            print("Enter the number of max members (or nothing)")
            max_members = input("#> ")
            print("Enter the number of min clan points (or nothing)")
            min_clan_level = input("#> ")
            print("Enter the number of max clan points (or nothing)")
            max_clan_level = input("#> ")
            filter = {
                "name": clan_name or None,
                "warFrequency": war_frequency or None,
                "locationId": location_id or None,
                "minMembers": min_members or None,
                "maxMembers": max_members or None,
                "minClanPoints": min_clan_level or None,
                "maxClanLevel": max_clan_level or None,
            }       
            print(clans.search_clans(ClansFilter(filter)))
        case '5':
            print("Enter the clan tag")
            clan_tag = coc_tag_input(input("#> "))
            print(clans.get_clan_current_war(clan_tag))
        case '6':
            print("Enter the clan tag")
            clan_tag = coc_tag_input(input("#> "))
            print(clans.get_clan_information(clan_tag))
        case '7':
            print("Enter the clan tag")
            clan_tag = coc_tag_input(input("#> "))
            print(clans.get_clan_list_members(clan_tag))
        case '8':
            print("Enter the clan tag")
            clan_tag = coc_tag_input(input("#> "))
            print(clans.get_clan_capital_raid_season(clan_tag))


def manage_goldpass_chioice(chosen_method):
    """
    Goldpass methods menu
    """
    match chosen_method:
        case '1':
            print(goldpass.get_goldpass_information())
            

def manage_locations_chioice(chosen_method):
    """
    Locations methods menu
    """
    match chosen_method:
        case '1':
            print("Enter the location id")
            location_id = input("#> ")
            print(locations.get_clan_rankings_for_location(location_id))
        case '2':
            print("Enter the location id")
            location_id = input("#> ")
            print(locations.get_player_rankings_for_location(location_id))
        case '3':
            print("Enter the location id")
            location_id = input("#> ")
            print(locations.get_player_builder_base_rankings_for_location(location_id))
        case '4':
            print("Enter the location id")
            location_id = input("#> ")
            print(locations.get_clans_builder_base_rankings_for_location(location_id))
        case '5':
            print("Enter the location id")
            print(locations.get_list_locations())
        case '6':
            print("Enter the location id")
            location_id = input("#> ")
            print(locations.get_capital_rankings_for_location(location_id))
        case '7':
            print("Enter the location id")
            location_id = input("#> ")
            print(locations.get_location_informations(location_id))


def manage_players_chioice(chosen_method):
    """
    Players methods menu
    """
    match chosen_method:
        case '1':
            print("Enter the player tag")
            player_tag = coc_tag_input(input("#> "))
            print("Enter the player API key")
            api_key = input("#> ")
            print(players.verify_player_token(player_tag, api_key))
        case '2':
            print("Enter the player tag")
            player_tag = coc_tag_input(input("#> "))
            print(players.get_player_information(player_tag))


def manage_labels_chioice(chosen_method):
    """
    Labels methods menu
    """
    match chosen_method:
        case '1':
            print(labels.get_labels_clans())
        case '2':
            print(labels.get_labels_players())


def manage_leagues_chioice(chosen_method):
    """
    Leagues methods menu
    """
    match chosen_method:
        case '1':
            print(leagues.get_list_capital_leagues())
        case '2':
            print(leagues.get_leagues())
        case '3':
            print("Enter the league id")
            league_id = input("#> ")
            print("Enter the season id")
            season_id = input("#> ")
            print(leagues.get_league_season_rankings(league_id, season_id))
        case '4':
            print("Enter the league id")
            league_id = input("#> ")
            print(leagues.get_capital_league_information(league_id))
        case '5':
            print("Enter the league id")
            league_id = input("#> ")
            print(leagues.get_builder_base_leagues_informations(league_id))
        case '6':
            print(leagues.get_list_builder_base_leagues())
        case '7':
            print("Enter the league id")
            league_id = input("#> ")
            print(leagues.get_league_informations(league_id))
        case '8':
            print("Enter the league id")
            league_id = input("#> ")
            print(leagues.get_league_seasons(league_id))
        case '9':
            print("Enter the league id")
            league_id = input("#> ")
            print(leagues.get_war_league_informations(league_id))
        case '9':
            print(leagues.get_list_war_leagues())