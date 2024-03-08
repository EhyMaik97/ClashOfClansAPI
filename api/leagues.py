"""
Calsh of Clans API - Leagues
"""
import requests
from utils.settings import ENDPOINT, define_correct_headers
from utils.helpers import print_url_and_sleep
import platform

headers = define_correct_headers(platform.system())


def get_list_capital_leagues():
    """
    List capital leagues

    API: /capitalleagues
    """
    url = f"{ENDPOINT}/capitalleagues"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_leagues():
    """
    List leagues

    API: /leagues
    """
    url = f"{ENDPOINT}/leagues"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_league_season_rankings(league_id: str, season_id: str):
    """
    Get league season rankings.
    Note that league season information is available only for Legend League.

    API: /leagues/{leagueId}/seasons/{seasonId}
    """
    url = f"{ENDPOINT}/leagues/{league_id}/seasons/{season_id}"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_capital_league_information(league_id: str):
    """
    Get capital league information

    API: /capitalleagues/{leagueId}
    """
    url = f"{ENDPOINT}/capitalleagues/{league_id}"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_builder_base_leagues_informations(league_id: str):
    """
    Get Builder Base league information

    API: /builderbaseleagues/{leagueId}
    """
    url = f"{ENDPOINT}/builderbaseleagues/{league_id}"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_list_builder_base_leagues():
    """
    List Builder Base leagues

    API: /builderbaseleagues
    """
    url = f"{ENDPOINT}/builderbaseleagues"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_league_informations(league_id: str):
    """
    Get league information

    API: /leagues/{leagueId}
    """
    url = f"{ENDPOINT}/leagues/{league_id}"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_league_seasons(league_id: str):
    """
    Get league seasons. 
    Note that league season information is available only for Legend League

    API: /leagues/{leagueId}/seasons
    """
    url = f"{ENDPOINT}/leagues/{league_id}/seasons"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_war_league_informations(league_id: str):
    """
    Get war league information

    API: /warleagues/{leagueId}
    """
    url = f"{ENDPOINT}/warleagues/{league_id}"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_list_war_leagues():
    """
    List war leagues

    API: /warleagues
    """
    url = f"{ENDPOINT}/warleagues"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()