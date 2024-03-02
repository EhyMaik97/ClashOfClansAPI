"""
Calsh of Clans API - Clans
"""
import requests
from models import clans_filter
from utils.settings import ENDPOINT, define_correct_headers
import platform
from dataclasses import asdict


headers = define_correct_headers(platform.system())

def get_clan_current_war_league_group(clan_tag: str):
    """
    Retrieve information about clan's current clan war league group

    API: /clans/{clanTag}/currentwar/leaguegroup
    """
    url = f"{ENDPOINT}/clans/{clan_tag.replace('#', '%23')}/currentwar/leaguegroup"
    print(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def get_clan_war_leagues(war_tag: str):
    """
    Retrieve information about individual clan war league war

    API: /clanwarleagues/wars/{warTag}
    """
    war_tag_fixed = war_tag.replace("#", "%23")
    url = f"{ENDPOINT}/clanwarleagues/wars/{war_tag_fixed}"
    print(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def get_clan_warlog(clan_tag: str):
    """
    Retrieve clan's clan war log

    API: /clan/{clanTag}/warlog
    """
    clan_tag_fixed = clan_tag.replace("#", "%23")
    url = f"{ENDPOINT}/clans/{clan_tag_fixed}/warlog"
    print(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def search_clans(clans_filter: clans_filter.ClansFilter):
    """
    Search clans based on filter criteria

    :param clans_filter: ClansFilter object containing filter criteria
    :return: JSON response containing search results
    """
    url = f"{ENDPOINT}/clans?"
    query_params = "&".join(
        [f"{key}={val}" for key, val in asdict(clans_filter).items() if val is not None]
    )
    url += query_params

    response = requests.get(url=url, headers=headers)
    return response.json()

def get_clan_current_war(clan_tag: str):
    """
    Retrieve information about clan's current clan war

    API: /clan/{clanTag}
    """
    clan_tag_fixed = clan_tag.replace("#", "%23")
    url = f"{ENDPOINT}/clans/{clan_tag_fixed}/currentwar"
    print(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def get_clan_information(clan_tag: str):
    """
    Get clan information

    API: /clan/{clanTag}
    """
    clan_tag_fixed = clan_tag.replace("#", "%23")
    url = f"{ENDPOINT}/clans/{clan_tag_fixed}"
    print(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def get_clan_list_members(clan_tag: str):
    """
    List clan members

    API: /clan/{clanTag}/members
    """
    clan_tag_fixed = clan_tag.replace("#", "%23")
    url = f"{ENDPOINT}/clans/{clan_tag_fixed}/members"
    print(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def get_clan_capital_raid_season(clan_tag: str):
    """
    Retrieve clan's capital raid seasons

    API: /clan/{clanTag}/capitalraidseasons
    """
    clan_tag_fixed = clan_tag.replace("#", "%23")
    url = f"{ENDPOINT}/clans/{clan_tag_fixed}/capitalraidseasons"
    print(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()