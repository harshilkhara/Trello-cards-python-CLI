import os
# Generate the TRELLO API AND TOKEN from here- https://trello.com/power-ups/admin

# For best practices
trello_api=os.environ.get('TRELLO_API')
trello_token=os.environ.get('TRELLO_TOKEN')

params = {
    'key': trello_api,
    'token': trello_token,
}
