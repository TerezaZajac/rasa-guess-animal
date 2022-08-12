# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import logging
from pprint import pformat
import re
from typing import Any, Text, Dict, List
import random
from unicodedata import name
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
# Animal.legs, color, size, food, movement, environment

class ActionPlayGuessAnimal(Action):

    def name(self) -> Text:
        animals = [
            {'legs':2, 'color': ['green'], 'size': 'small', 'food': ['insect'], 'habitation': 'It lives in a large number of environments from tropical forests to frozen tundras to deserts but mostly in aquatic and swampy habitats', 'name': 'frog'}, 
            {'legs':4, 'color': ['black', 'white'], 'size': 'big', 'food': ['bamboo'], 'habitation': 'It lives in forests high in the mountains of southwest China','name': 'panda'}, 
            {'legs':2, 'color': ['black'], 'size': 'small', 'food': ['insect'], 'habitation': 'It lives all over the world—in caves and trees, under bridges, and in mines and other structures','name': 'bat'}, 
            {'legs':2, 'color': ['green', 'yellow', 'oragne', 'red'], 'size': 'small', 'food': ['seeds', 'nuts', 'fruits', 'vegetable', 'leaves'], 'habitation': 'It lives in warm climates all over the world. The greatest diversities exist in Australasia, Central America, and South America.','name': 'parrot'}, 
            {'legs':4, 'color': ['brown'], 'size': 'big', 'food': ['fish', 'berries', 'meat', 'honey'], 'habitation': 'It lives in forests, mountains, tundra, deserts and grassy areas all over the world.','name': 'bear'}, 
            {'legs':4, 'color': ['orange', 'black'], 'size': 'big', 'food': ['meat'], 'habitation': 'It lives in the Siberian taiga, swamps, grasslands, and rainforests. It can be found anywhere from the Russian Far East to parts of North Korea, China, India, Southwest Asia and the Sumatra','name': 'tiger'}, 
            {'legs':6, 'color': ['yellow', 'black'], 'size': 'small', 'food': ['flowers'], 'habitation': 'It lives all over the world.','name': 'bee'}, 
            {'legs':0, 'color': ['grey'], 'size': 'big', 'food': ['fish'], 'habitation': 'It lives in the ocean or waters along coastlines.','name': 'dolphin'}, 
            {'legs':0, 'color': ['brown', 'green', 'white', 'yellow', 'black'], 'size': 'medium', 'food': ['mice', 'meat', 'rodents'], 'habitation': ['It lives in Asia, Africa, and Australia.'], 'name': 'python'}, 
            {'legs':8, 'color': ['black'], 'size': 'small', 'food': ['insect'], 'habitation': 'It lives outdoor and indoor all over the world.','name': 'spider'}
            ]
        
        self.animal = animals[random.randint(0, len(animals)-1)]

        return 'action_play_guess'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        #logging.info(tracker.latest_message)
        logging.info(tracker.get_slot('color'))
        logging.info(tracker.get_slot('legs'))
        logging.info(tracker.get_slot('animal'))
    
        
        if tracker.get_intent_of_latest_message() == 'legs':
            legs = re.findall('\d', tracker.latest_message['text'])
            if len(legs) and int(legs[0]) == self.animal['legs']:
                dispatcher.utter_message(text=f'Yes, it has {legs[0]} legs')
            elif len(legs):
                dispatcher.utter_message(text=f'No it does not have {legs[0]} legs')
            else:
                dispatcher.utter_message(text=f'It has {self.animal["legs"]} legs')
            return []


        if tracker.get_intent_of_latest_message() == 'color':
            if tracker.get_slot('color') in self.animal['color']:
                if len(self.animal['color']) == 1:
                    dispatcher.utter_message(text=f'Yes it is {self.animal["color"]}!')
                else:
                    dispatcher.utter_message(text=f'Yes it is one of its colors!')
            else:
                dispatcher.utter_message(text=f'No, it is not {tracker.get_slot("color")}!')
            return []

        message = tracker.latest_message['text']
        if tracker.get_intent_of_latest_message() == 'size':
            if message.find('how') == 0 or message.find('what') == 0:
                dispatcher.utter_message(text=f'It is {self.animal["size"]}')
            elif tracker.get_slot('size') == self.animal['size']:
                dispatcher.utter_message(text=f'Yes, it is {self.animal["size"]}')
            else:
                dispatcher.utter_message(text=f'No, it is not {tracker.get_slot("size")}')
            return []

        if tracker.get_intent_of_latest_message() == 'habitation':
            dispatcher.utter_message(text=f'{self.animal["habitation"]}')
        
        if tracker.get_intent_of_latest_message() == 'food':
            dispatcher.utter_message(text=f'I eats {self.animal["food"]}')

        if tracker.get_intent_of_latest_message() == 'animal':
            if tracker.get_slot('animal') == self.animal['name']:
                dispatcher.utter_message(text=f'Very good, it is a {self.animal["name"]}')
                dispatcher.utter_message(response='utter_play_again');
            else:
                dispatcher.utter_message(text=f'Sorry, but it is not a {tracker.get_slot("animal")}')
            return []
        
        #dispatcher.utter_message(text="Perfect")
        #dispatcher.utter_message(response = 'utter_play_again')

        return []