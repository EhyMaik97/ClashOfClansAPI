"""
Calsh of Clans API - helpers
"""
import importlib
import time

def print_url_and_sleep(url):
    print(f"Sendig request to: {url}")
    time.sleep(2)

def show_menu():
    print("Choose an API service:")
    print("1. Clans")
    print("2. Esports")
    print("3. Goldpass")
    print("4. Labels")
    print("5. Leagues")
    print("6. Locations")
    print("7. Players")
    print("0. Exit")


def get_methods_from_module(module_name):
    try:
        spec = importlib.util.spec_from_file_location(module_name, f"api/{module_name}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return [
            method for method in dir(module) if callable(getattr(module, method)) 
                and method.startswith("get_") 
                or method.startswith("search_")
        ]
    except FileNotFoundError:
        print(f"Module: {module_name}.py not found.")
        return []

def show_methods_menu(methods):
    print("Select a method:")
    for index, method in enumerate(methods, start=1):
        print(f"{index}. {method}")

def get_parameters(method_name):
    parameters = {}
    while True:
        if method_name == "get_clan_current_war":
            clan_tag = input("Inserisci il tag del clan (es. #ABC123): ")
            parameters["clan_tag"] = clan_tag
            break
    return parameters