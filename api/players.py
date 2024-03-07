"""
Calsh of Clans API - Players
"""
import requests
from utils.settings import ENDPOINT, define_correct_headers
from utils.helpers import print_url_and_sleep
import platform

headers = define_correct_headers(platform.system())

def verify_player_token(player_tag: str):
    """
    Verify player API token 

    API: /players/{playerTag}/verifytoken
    """
    player_tag_fixed = player_tag.replace("#", "%23")
    url = f"{ENDPOINT}/players/{player_tag_fixed}/verifytoken"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def get_player_information(player_tag: str):
    """
    Get player informations

    API: /players/{playerTag}
    """
    player_tag_fixed = player_tag.replace("#", "%23")
    url = f"{ENDPOINT}/players/{player_tag_fixed}"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()