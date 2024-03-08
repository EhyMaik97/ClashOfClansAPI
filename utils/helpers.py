"""
Calsh of Clans API - helpers
"""
import time


def print_url_and_sleep(url: str):
    """
    Takes a url string as input, print a sending message
    and wait 2 seconds.
    """
    print(f"Sendig request to: {url}")
    time.sleep(2)


def coc_tag_input(command_input: str):
    """
    This function takes a string as input, converts it to uppercase, 
    and adds a "#" if it isn't already present at the beginning.
    """
    if not command_input.startswith("#"):
        command_input = "#" + command_input
    return command_input.upper()