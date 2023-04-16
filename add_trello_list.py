import requests
import argparse
from config import *

'''
This is implementation of adding a list to trello.com board mentioned in next development steps in README.md
'''

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Add a list to a Trello board.')
parser.add_argument('board_id', type=str, help='the ID of the Trello board')
parser.add_argument('list_name', type=str, help='the name of the Trello column')
args = parser.parse_args()

# Getting the board id
board_id=args.board_id
url = f"https://api.trello.com/1/boards/{board_id}/lists"

# Adding a new list to the board
params['name']=args.list_name
response=requests.post(url, params=params)
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

ls=response.json()
# Printing the created list name and ID 
print(f"Created list {args.list_name}: {ls['id']}")
