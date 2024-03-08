"""
Calsh of Clans API - Locations
"""
import requests
from utils.settings import ENDPOINT, get_headers
from utils.helpers import print_url_and_sleep
import platform

headers = get_headers()

def get_clan_rankings_for_location(location_id: str):
    """
    Get clan rankings for a specific location

    API: /locations/{locationId}/rankings/clans
    """
    url = f"{ENDPOINT}/locations/{location_id}/rankings/clans"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_player_rankings_for_location(location_id: str):
    """
    Get player rankings for a specific location

    API: /locations/{locationId}/rankings/players
    """
    url = f"{ENDPOINT}/locations/{location_id}/rankings/players"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_player_builder_base_rankings_for_location(location_id: str):
    """
    Get player Builder Base rankings for a specific location

    API: /locations/{locationId}/rankings/players-builder-base
    """
    url = f"{ENDPOINT}/locations/{location_id}/rankings/players-builder-base"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_clans_builder_base_rankings_for_location(location_id: str):
    """
    Get clan Builder Base rankings for a specific location

    API: /locations/{locationId}/rankings/clans-builder-base
    """
    url = f"{ENDPOINT}/locations/{location_id}/rankings/clans-builder-base"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_list_locations():
    """
    List locations

    API: /locations
    """
    url = f"{ENDPOINT}/locations"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_capital_rankings_for_location(location_id: str):
    """
    Get capital rankings for a specific location

    API: /locations/{locationId}/rankings/capitals
    """
    url = f"{ENDPOINT}/locations/{location_id}/rankings/capitals"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_location_informations(location_id: str):
    """
    Get information about specific location

    API: /locations/{locationId}
    """
    url = f"{ENDPOINT}/locations/{location_id}"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()