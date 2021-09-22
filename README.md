# ChatBot

Accompanying repository for creating a django based bot server that uses django-channels for  WebSockets connection. This is an additional feature implementation of the code available at https://github.com/vaisaghvt/django-bot-server-tutorial/

# Additional features added
- Chat Bot now presents 3 buttons to users “stupid”, “fat”, “dumb”. When a user clicks a button the appropriate joke is displayed to them.
- Postgres database model that records the number of calls to each of the buttons.
- User ID is now just made to be an integer value which will appear on the title of the browser page. New user will be added when page is refreshed.
- Stores the number of calls on a per user basis. 
- Number of calls to each buttin by users can be viewed by clicking the 'Check Button Usage' button. This will navigate to a simple web page with a table showing all the users and the number of calls they have made.

# How to use this branch

To get this running, simply run the following 

## Step 1: Install req.txt

`pip install -r requirement.txt`

## Step 2: Create databases
Install PostgreSQL - 9.3.25 and db - newdb , user - dbuser, password - dbpass (This can be changed, remember to update it in the settings.py)
Create the databases and the initial migrations with the following command:
`python manage.py makemigrations`

`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ and chat with the bot
