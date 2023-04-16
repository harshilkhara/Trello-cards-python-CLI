import requests
import argparse
from config import *

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Add a card to a Trello board.')
parser.add_argument('board_id', type=str, help='the ID of the Trello board')
parser.add_argument('column_name', type=str, help='the name of the Trello column')
parser.add_argument('card_name', type=str, help='the name of the Trello card')
parser.add_argument('-c', '--comment', type=str, help='a comment for the Trello card')
parser.add_argument('-l', '--labels', nargs='+', type=str, help='labels for the Trello card')
args = parser.parse_args()


# Get the ID of the specified column by name
column_url = f"https://api.trello.com/1/boards/{args.board_id}/lists"
response = requests.get(column_url, params=params)
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()
lists = response.json()
column_id = None
for l in lists:
    if l['name'].lower() == args.column_name.lower():
        column_id = l['id']
        break
if column_id is None:
    print(f"Column '{args.column_name}' not found.")
    exit()

# Create the Trello card
params['idList'] = column_id
params['name'] = args.card_name
if args.comment:
    params['desc'] = args.comment

card_url = f"https://api.trello.com/1/cards"
response = requests.post(card_url, params=params)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()
card = response.json()


#Get the newly created card and add a label if any
if args.labels:
    card_id=card['id']
    url = f"https://api.trello.com/1/cards/{card_id}/labels"
    for col in args.labels:
        params['color']=col
        response = requests.post(url, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code} : Invalid color label")


# Print the URL of the created card
print(f"Card created: {card['url']}")
