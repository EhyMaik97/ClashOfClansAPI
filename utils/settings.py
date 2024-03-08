"""
Calsh of Clans API - settings
"""
ENDPOINT = "https://api.clashofclans.com/v1"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc2OGJkNDEwLWE3MjItNGJhYy05MGRiLWI4MWY1ZTlhMjVmNSIsImlhdCI6MTcwOTkxMzc5OSwic3ViIjoiZGV2ZWxvcGVyLzZhNWU0OTI4LWY3OTItYWE5Ni0wYTBmLTIwNjRlYzhmNzlhNiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4OC4yMTcuMjI4LjQiXSwidHlwZSI6ImNsaWVudCJ9XX0.1ipXk9QtUerXuGgURSlgCBmskD6whhVGF1YWuoGDxC-udIEN5erZBwF8PjOnhtnjpWpd4sDD7edU_YJZmZ-ckQ"

def get_headers():
    headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + API_TOKEN
        }
    return headers