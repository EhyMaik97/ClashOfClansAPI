"""
Clash of Clans API - main
"""
from models import clans_filter
from api import clans, esports, goldpass, labels, leagues, locations, players

def main():
    filter = clans_filter.ClansFilter(
        name="test",
        limit=1
    )
    # clans.search_clans(filter)

    print(players.get_player_information("#2LYUJ82G9"))

if __name__ == "__main__":
    main()