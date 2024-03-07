"""
Calsh of Clans API - GoldPass
"""
import requests
from utils.settings import ENDPOINT, define_correct_headers
from utils.helpers import print_url_and_sleep
import platform

headers = define_correct_headers(platform.system())

def get_goldpass_information():
    """
    Access information about the current goldpass season

    API: goldpass/seasons/current
    """
    url = f"{ENDPOINT}/goldpass/seasons/current"
    print_url_and_sleep(url)
    response = requests.get(url=url, headers=headers)
    
    return response.json()