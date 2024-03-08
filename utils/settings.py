"""
Calsh of Clans API - settings
"""
ENDPOINT = "https://api.clashofclans.com/v1"
API_TOKEN = ""

def get_headers():
    headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + API_TOKEN
        }
    return headers