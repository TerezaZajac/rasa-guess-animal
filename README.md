# rasa-guess-animal
Rasa AI, guess animal game

## description
Create a simple chatbot for playing an animal guessing game using the Rasa framework (https://rasa.com/docs/rasa/) with simple intents and entities.

Bot:  Try to guess the animal I am thinking of.

(recognize user-defined entities, e.g.)

User: Is it brown?

Bot:  No, it is not brown.

User: How many legs does it have?

Bot:  It has four legs.

User: Does it jump?

Bot: Yes, it can jump.

User: Is it a frog?

Bot: Congratulations, you guessed it correctly, it is a frog indeed.

## install python enviroment
```sh
brew install pyenv
pyenv install 3.8.10    #rasa needs python 3.7 or 3.8

sudo /Users/user/.pyenv/versions/3.8.10/bin/python3 -m venv venv 
```

```sh
source ./venv/bin/activate
```

## instal and run rasa
```sh
pip install rasa
```

terminal1:
```sh
    rasa init           #instal of demo bot
    rasa train          #to train bot
    rasa shell          #to run bot
```
terminal2:
```sh
    rasa run actions    #to run py
```
