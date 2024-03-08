"""
Calsh of Clans API - settings
"""
ENDPOINT = "https://api.clashofclans.com/v1"
API_TOKEN_WINDOWS = ""
API_TOKEN_LINUX = ""

def define_correct_headers(os_name):
    headers = {
            'Accept': 'application/json',
        }
    if os_name == "Linux":
        headers.update({
            'Authorization': 'Bearer ' + API_TOKEN_LINUX
        })
    else:
        headers.update({
            'Authorization': 'Bearer ' + API_TOKEN_WINDOWS
        })
    return headers