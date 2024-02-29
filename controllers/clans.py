"""
Calsh of Clans API - Clans
"""
import requests
from models import clans_filter

# from utils.settings import ENDPOINT, headers
ENDPOINT = "https://api.clashofclans.com/v1"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZhZDZhNDYzLThmZWQtNGJjZC1hMTY3LTY3YTE4NzYyNDZkMiIsImlhdCI6MTcwOTIwNjkyMSwic3ViIjoiZGV2ZWxvcGVyLzZhNWU0OTI4LWY3OTItYWE5Ni0wYTBmLTIwNjRlYzhmNzlhNiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwOS4xMTYuMjIzLjkwIl0sInR5cGUiOiJjbGllbnQifV19.jMb6WtqX83ypccHrLHa1RsHtYF4N30xC7lAaROvXY5fLHNh4R3m-ImDr0rUcDlXnJwRAhdfCRvyuiqcaOnQ1Kg"
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + API_TOKEN
}

def get_clan_current_war_league_gruop(clan_tag: str):
    """
    Retrieve information about clan's current clan war league group

    API: /clans/{clanTag}/currentwar/leaguegroup
    """
    url = (f"{ENDPOINT}/clans/{clan_tag.replace("#", "%23")}/currentwar/leaguegroup")
    print(url)
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()

def get_clan_war_leagues(war_tag: str):
    """
    Retrieve information about individual clan war league war

    API: /clanwarleagues/wars/{warTag}
    """
    url = (f"{ENDPOINT}/clanwarleagues/wars/{war_tag.replace("#", "%23")}")
    print(url)
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()

def get_clan_warlog(clan_tag: str):
    """
    Retrieve clan's clan war log

    API: /clan/{clanTag}/warlog
    """
    url = (f"{ENDPOINT}/clans/{clan_tag.replace("#", "%23")}/warlog")
    print(url)
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()

def search_clans(dict_filter: dict):
    """
    Search clans

    API: /clans/
    """
    url = (f"{ENDPOINT}/clans?")
    for key, vals in dict_filter.items():
        url.append(f"&{key}={vals}")
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()

def get_clan_current_war(clan_tag: str):
    """
    Retrieve information about clan's current clan war

    API: /clan/{clanTag}
    """
    url = (f"{ENDPOINT}/clans/{clan_tag.replace("#", "%23")}/currentwar")
    print(url)
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()

def get_clan_information(clan_tag: str):
    """
    Get clan information

    API: /clan/{clanTag}
    """
    url = (f"{ENDPOINT}/clans/{clan_tag.replace("#", "%23")}")
    print(url)
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()

def get_clan_list_members(clan_tag: str):
    """
    List clan members

    API: /clan/{clanTag}/members
    """
    url = (f"{ENDPOINT}/clans/{clan_tag.replace("#", "%23")}/members")
    print(url)
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()

def get_clan_capital_raid_season(clan_tag: str):
    """
    Retrieve clan's capital raid seasons

    API: /clan/{clanTag}/capitalraidseasons
    """
    url = (f"{ENDPOINT}/clans/{clan_tag.replace("#", "%23")}/capitalraidseasons")
    print(url)
    response = requests.get(url=url, headers=headers)
    print(response.json())
    return response.json()


search_clans({"name":"test", "limit":1})