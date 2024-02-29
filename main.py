"""
Clash of Clans API - main
"""
from models import clans_filter
from controllers import clans, esports, goldpass, labels, leagues, locations, players

def main():
    filter = clans_filter.ClansFilter(
        name="test",
        limit=1
    )
    clans.search_clans(filter)

if __name__ == "__main__":
    main()