# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import logging
from typing import Any, Text, Dict, List
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
 
# Animal.legs, color, size, food, movement, habitation

class ActionPlayGuessAnimal(Action):
    animal = None
    def name(self) -> Text:
        return 'action_play_guess'
    
    def shuffle(self):
        animals = [
            {'legs':[4, 'four'], 'color': ['green'], 'size': 'small', 'food': ['insect'], 'status': 'insectivore', 'habitation': 'It lives in a large number of environments from tropical forests to frozen tundras to deserts but mostly in aquatic and swampy habitats', 'movement':['jump', 'swim'], 'name': 'frog'}, 
            {'legs':[4, 'four'], 'color': ['black', 'white'], 'size': 'big', 'food': ['bamboo'], 'status': 'herbivore', 'habitation': 'It lives in forests high in the mountains of southwest China', 'movement':['run', 'climb'], 'name': 'panda'}, 
            {'legs':[2,'two'], 'color': ['black'], 'size': 'small', 'food': ['insect'], 'status': 'insectivore',  'habitation': 'It lives all over the world—in caves and trees, under bridges, and in mines and other structures','movement':['fly'], 'name': 'bat'}, 
            {'legs':[2,'two'], 'color': ['green', 'yellow', 'oragne', 'red'], 'size': 'small', 'food': ['seeds', 'nuts', 'fruits', 'vegetable', 'leaves'], 'status': 'herbivore', 'habitation': 'It lives in warm climates all over the world. The greatest diversities exist in Australasia, Central America, and South America.','movement':['fly'], 'name': 'parrot'}, 
            {'legs':[4, 'four'], 'color': ['brown'], 'size': 'big', 'food': ['fish', 'berries', 'meat', 'honey'], 'status': 'omnivore',  'habitation': 'It lives in forests, mountains, tundra, deserts and grassy areas all over the world.','movement':['run', 'climb'],'name': 'bear'}, 
            {'legs':[4, 'four'], 'color': ['orange', 'black'], 'size': 'big', 'food': ['meat'], 'status': 'carnivore', 'habitation': 'It lives in the Siberian taiga, swamps, grasslands, and rainforests. It can be found anywhere from the Russian Far East to parts of North Korea, China, India, Southwest Asia and the Sumatra','movement':['run', 'crawl'],'name': 'tiger'}, 
            {'legs':[6,'six'], 'color': ['yellow', 'black'], 'size': 'small', 'food': ['flowers'], 'status': 'herbivore', 'habitation': 'It lives all over the world.','movement':['fly'], 'name': 'bee'}, 
            {'legs':[0,'zero'], 'color': ['grey'], 'size': 'big', 'food': ['fish', 'meat'], 'status': 'carnivore', 'habitation': 'It lives in the ocean or waters along coastlines.','movement':['swim', 'jump'], 'name': 'dolphin'}, 
            {'legs':[0,'zero'], 'color': ['brown', 'green', 'white', 'yellow', 'black'], 'size': 'medium', 'food': ['mice', 'meat', 'rodents'], 'status': 'carnivore', 'habitation': ['It lives in Asia, Africa, and Australia.'], 'movement':['crawl'], 'name': 'python'}, 
            {'legs':[8,'eight'], 'color': ['black'], 'size': 'small', 'food': ['insect'], 'status': 'insectivore', 'habitation': 'It lives outdoor and indoor all over the world.','movement':['run', 'crawl'], 'name': 'spider'}
            ]
        
        self.animal = animals[random.randint(0, len(animals)-1)]
       
    def is_w_question(self, message):
        return message.find('how') == 0 or message.find('what') == 0 or message.find('where') == 0

    def lst_to_srt(self, title):
        return (', '.join(title))

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not self.animal:
             self.shuffle()

        #logging.info(tracker.latest_message)
        logging.info(tracker.get_slot('color'))
        logging.info(tracker.get_slot('legs'))
        logging.info(tracker.get_slot('animal'))
        
        message = tracker.latest_message['text']
        legs = tracker.get_slot('legs')
        if tracker.get_intent_of_latest_message() == 'legs':
            if self.is_w_question(message):
                dispatcher.utter_message(text=f'It has {self.animal["legs"][0]} legs')
            elif legs == None: 
                if self.animal['legs'][0] == 0: 
                    dispatcher.utter_message(text=f'It does not have any legs.')
                else:
                    dispatcher.utter_message(text=f'it has some legs.') 
            elif legs in self.animal['legs']:
                dispatcher.utter_message(text=f'Yes, it has {legs} legs')
            else:
                dispatcher.utter_message(text=f'No it does not have {legs} legs')
            return []

        if tracker.get_intent_of_latest_message() == 'color':
            if self.is_w_question(message):
                dispatcher.utter_message(text=f'It is {self.lst_to_srt(self.animal["color"])}.')
            elif tracker.get_slot('color') in self.animal['color']:
                if len(self.animal['color']) == 1:
                    dispatcher.utter_message(text=f'Yes it is {self.lst_to_srt(self.animal["color"])}!')
                else:
                    dispatcher.utter_message(text=f'Yes it is one of its colors!')
            else:
                dispatcher.utter_message(text=f'No, it is not {tracker.get_slot("color")}!')
            return [SlotSet("color", None)]

        if tracker.get_intent_of_latest_message() == 'size':
            if self.is_w_question(message):
                dispatcher.utter_message(text=f'It is {self.animal["size"]}')
            elif tracker.get_slot('size') == self.animal['size']:
                dispatcher.utter_message(text=f'Yes, it is {self.animal["size"]}')
            else:
                dispatcher.utter_message(text=f'No, it is not {tracker.get_slot("size")}')
            return []
        
        if tracker.get_intent_of_latest_message() == 'movement':
            if message.find('how') == 0 or message.find('what') == 0:
                dispatcher.utter_message(text=f'It can {self.lst_to_srt(self.animal["movement"])}.')
            elif tracker.get_slot('movement') in self.animal['movement']:
                if len(self.animal['movement']) == 1:
                    dispatcher.utter_message(text=f'Yes it can {self.lst_to_srt(self.animal["movement"])}!')
                else:
                    dispatcher.utter_message(text=f'Yes it can {tracker.get_slot("movement")} and more!')
            else:
                dispatcher.utter_message(text=f'No, it cannot {tracker.get_slot("movement")}.')
            return []

        if tracker.get_intent_of_latest_message() == 'food':
            if message.find('how') == 0 or message.find('what') == 0:
                dispatcher.utter_message(text=f'It eats {self.lst_to_srt(self.animal["food"])}. It is a {self.animal["status"]}.')
            elif tracker.get_slot('food') in self.animal['food']:
                if len(self.animal['food']) == 1:
                    dispatcher.utter_message(text=f'Yes it eats {self.lst_to_srt(self.animal["food"])}! It is a {self.animal["status"]}.')
                else:
                    dispatcher.utter_message(text=f'Yes it eats {tracker.get_slot("food")} and more! It is a {self.animal["status"]}.')
            else:
                dispatcher.utter_message(text=f'No, it does not eat {tracker.get_slot("food")}. It is a {self.animal["status"]}.')
            return []
        
        if tracker.get_intent_of_latest_message() == 'habitation':
            dispatcher.utter_message(text=f'{self.animal["habitation"]}')
        
        if tracker.get_intent_of_latest_message() == 'animal':
            if tracker.get_slot('animal') == self.animal['name']:
                dispatcher.utter_message(text=f'Very good, it is a {self.animal["name"]}!')
                dispatcher.utter_message(response='utter_play_again')  
                self.shuffle()
            else:
                dispatcher.utter_message(text=f'Sorry, but it is not a {tracker.get_slot("animal")}.')
            return [
                SlotSet("legs", None),
                SlotSet("color", None),
                SlotSet("animal", None),
                SlotSet("size", None),
                SlotSet("food", None),
                SlotSet("movement", None)
                ]
        
        #dispatcher.utter_message(text="Perfect")
        #dispatcher.utter_message(response = 'utter_play_again')

        return []