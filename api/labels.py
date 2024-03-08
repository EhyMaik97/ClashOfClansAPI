"""
Calsh of Clans API - Labels
"""

import requests
from utils.settings import ENDPOINT, define_correct_headers
from utils.helpers import print_url_and_sleep
import platform

headers = define_correct_headers(platform.system())


def get_labels_players():
    """
    List player labels

    API: /labels/players
    """
    url = f"{ENDPOINT}/labels/players"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()


def get_labels_clans():
    """
    List clan labels

    API: /labels/clan
    """
    url = f"{ENDPOINT}/labels/clan"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()