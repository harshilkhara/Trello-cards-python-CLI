# Project Description 

A CLI program which adds a new card to a trello.com board. The program takes the user input to add a 
Trello card with labels and a comment to the specified column of board. The project also includes an 
extra implementation of adding a new list/ column to trello.com board with further steps of development 
process discussed which will help this project to scale up. The project also follows the best practices 
in the industry.

# How to get started 

1. Generate the Trello API and token from here- https://trello.com/power-ups/admin

2. Set the environment variables for Trello API and Token. 
    Steps to set enviroment variables 
	If you are on macOS- 

	i) Open terminal

	ii) Enter the command: `sudo nano ~/.zshrc`

	Now write the following variables in the editor- 

	```
	TRELLO_API="Enter your trello api here"
	TRELLO_TOKEN="Enter your trello token here"
	```

	iii) Save the above changes in nano editor and restart the terminal.

3. If you are having trouble in step 2, you can open config.py file and write your trello API and token directly there.

4. Install all the dependencies from requirements.txt by running in console - ` pip install -r requirements.txt `

5. Now create a trello board in your trello.com. The board’s ID will be the string of characters that comes after “https://trello.com/b/”. 
    For example, in the URL “https://trello.com/b/abcdef123456789/my-board”, the board’s ID would be “abcdef123456789”

6. To add a trello card with labels and a comment run the script in command line with following arguments- 

    i) Before running the script understand the arguments the script takes- 
        
        Run the below command to get a list of all positional and optional arguments- 
            python3 add_trello_card.py -h 

        You will see the following output- 

        ```
        usage: add_trello_card.py [-h] [-c COMMENT] [-l LABELS [LABELS ...]] board_id column_name card_name

        Add a card to a Trello board.

        positional arguments:
        board_id              the ID of the Trello board
        column_name           the name of the Trello column
        card_name             the name of the Trello card

        optional arguments:
        -h, --help            show this help message and exit
        -c COMMENT, --comment COMMENT
                                a comment for the Trello card
        -l LABELS [LABELS ...], --labels LABELS [LABELS ...]
                                labels for the Trello card
        ```
    which equates to- 
    ```
        python3 add_trello_card.py BOARD_ID "your list name/ specified column"  "your card name" -c "your comment" -l "your color1" "your color2"
    ```

    For example- 
        python3 add_trello_card.py ABCDEF123 "To do" "A new card" -c "sprint 1" -l "yellow" "green" 

    The above will now add a card with name "A new card" to the "To do" specified column in your trello board with comment "sprint 1" and 
    label it with yellow and green color.

7. The next development steps would be- 

    i) We can also implement a script which adds a new column/ list to the trello board. 
        I have implemented this script and documented it in step 8. 
    
    ii) We can also implement other scripts which can update a card, create a new checklist on card 
        using the similar technique and scale this project up. 

8. To add a trello list to the board run the script in command line with following arguments- 

    i) Before running the script understand the arguments the script takes- 
        
        Run the below command to get a list of all positional and optional arguments- 
            python3 add_trello_list.py -h

        You will see the following output- 
        ```
        usage: add_trello_list.py [-h] board_id list_name

        Add a list to a Trello board.

        positional arguments:
        board_id    the ID of the Trello board
        list_name   the name of the Trello column

        optional arguments:
        -h, --help  show this help message and exit
        ```
    which equates to- 

    ```
        python3 add_trello_list.py BOARD_ID "your list name/ specified column"
    ```

    For example- 
        python3 add_trello_list.py ABCDEF123 "a new list"

    The above will now add a column/ list with name "a new list" to the trello board.

