"""
Calsh of Clans API - GoldPass
"""
import requests
from utils.settings import ENDPOINT, get_headers
from utils.helpers import print_url_and_sleep

headers = get_headers()


def get_goldpass_information():
    """
    Access information about the current goldpass season

    API: goldpass/seasons/current
    """
    url = f"{ENDPOINT}/goldpass/seasons/current"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()