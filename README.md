## README.me - Clash of Clans API Terminal Interface

This project implements a simple terminal interface for interacting with the Clash of Clans API. 

### Features

* Retrieve information about clans, players, location and others
* Interact with the API using a user-friendly menu.

**Note:** This is a basic implementation and may not include all functionalities of the Clash of Clans API. 

### Dependencies

* Python 3 (tested with version 3.12)
* Requests library (`pip install requests`) - for making API requests

### Installation

1. Clone this repository or download the files.
2. Install the `requests` library using `pip install requests` in your terminal.

### Usage

1. Login on https://developer.clashofclans.com and from the account, create the API key with your IP
2. Go on _utils/setting.py_ and set the API_TOKEN created in 1.
1. Open a terminal and navigate to the directory containing the Python script.
2. Run the script using `python main.py`.
3. Follow the on-screen instructions to interact with the API.

**Example:**

```
Welcome to the Clash of Clans Terminal Interface!

1. Get information about Clans
2. Get information about Goldpass
3. Get information about Locations
4. Get information about Players
.
.
.
0. Exit

Enter your choice: 
```

### Contributing

Pull requests and suggestions are welcome!