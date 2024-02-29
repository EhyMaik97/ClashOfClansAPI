"""
Calsh of Clans API - settings
"""
ENDPOINT = "https://api.clashofclans.com/v1"
API_TOKEN_WINDOWS = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZhZDZhNDYzLThmZWQtNGJjZC1hMTY3LTY3YTE4NzYyNDZkMiIsImlhdCI6MTcwOTIwNjkyMSwic3ViIjoiZGV2ZWxvcGVyLzZhNWU0OTI4LWY3OTItYWE5Ni0wYTBmLTIwNjRlYzhmNzlhNiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwOS4xMTYuMjIzLjkwIl0sInR5cGUiOiJjbGllbnQifV19.jMb6WtqX83ypccHrLHa1RsHtYF4N30xC7lAaROvXY5fLHNh4R3m-ImDr0rUcDlXnJwRAhdfCRvyuiqcaOnQ1Kg"
API_TOKEN_LINUX = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM3ZWFmOTJiLTZhY2UtNGY2NS05NTI1LWVhYzdjN2FmYzUwYSIsImlhdCI6MTcwOTI0NDM1Miwic3ViIjoiZGV2ZWxvcGVyLzZhNWU0OTI4LWY3OTItYWE5Ni0wYTBmLTIwNjRlYzhmNzlhNiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjIuNDIuMTcwLjc2Il0sInR5cGUiOiJjbGllbnQifV19._DzN9ULZ-C_z-YHYjTrWlDQ5PDGBiHtmSxj6wsonEcSm3Jar84FeexoCKz0X_uCfxRS0i1yjNjT2jT_2XDFn4Q"

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