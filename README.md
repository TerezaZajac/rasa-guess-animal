# rasa-guess-animal
Rasa AI, guess animal game

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
