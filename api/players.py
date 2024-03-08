"""
Calsh of Clans API - Players
"""
import requests
from utils.settings import ENDPOINT, get_headers
from utils.helpers import print_url_and_sleep

headers = get_headers()


def verify_player_token(player_tag: str, api_key: str):
    """
    Verify player API token 

    API: /players/{playerTag}/verifytoken
    """
    player_tag_fixed = player_tag.replace("#", "%23")
    url = f"{ENDPOINT}/players/{player_tag_fixed}/verifytoken"
    body = {
        "token": api_key
    }
    print_url_and_sleep(url)
    response = requests.post(url=url, headers=headers, json=body)
    
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