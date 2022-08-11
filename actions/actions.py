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
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence

# Animal.legs, color, size, food, movement, environment

class ActionPlayGuessAnimal(Action):

    def name(self) -> Text:
        self.animal = {'legs':2, 'color': 'green', 'name': 'frog'}

        return "action_play_guess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        logging.info(tracker.get_intent_of_latest_message())
        logging.info(tracker.get_slot("color"))
        logging.info(tracker.get_slot("legs"))
        logging.info(tracker.get_slot("animal"))
    
        
        if tracker.get_intent_of_latest_message() == 'legs':
            legs = re.findall("\d", tracker.latest_message['text'])
            if len(legs) and int(legs[0]) == self.animal['legs']:
                dispatcher.utter_message(text=f"Yes, it has {legs[0]} legs")
                return []
            elif len(legs):
                dispatcher.utter_message(text=f"No it has not {legs[0]} legs")
                return []
            else:
                dispatcher.utter_message(text=f"It has {self.animal['legs']} legs")
                return []
        elif tracker.get_intent_of_latest_message() == 'color':
            if tracker.get_slot("color") == self.animal['color']:
                dispatcher.utter_message(text=f"Yes it is {self.animal['color']}!")
                return []
            else:
                dispatcher.utter_message(text=f"No, it is not {tracker.get_slot('color')}!")
                return []
        
        
        #dispatcher.utter_message(text="Perfect")
        #dispatcher.utter_message(response = 'utter_play_again')

        return []

class ActionPlayRPS(Action):
   
    def name(self) -> Text:
        return "action_play_rps"
 
    def computer_choice(self):
        generatednum = random.randint(1,3)
        if generatednum == 1:
            computerchoice = "rock"
        elif generatednum == 2:
            computerchoice = "paper"
        elif generatednum == 3:
            computerchoice = "scissors"
       
        return(computerchoice)
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # play rock paper scissors
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"You chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The computer chose {comp_choice}")
 
        if user_choice == "rock" and comp_choice == "scissors":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "rock" and comp_choice == "paper":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "paper" and comp_choice == "rock":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "paper" and comp_choice == "scissors":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "scissors" and comp_choice == "paper":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "scissors" and comp_choice == "rock":
            dispatcher.utter_message(text="The computer won this round.")
        else:
            dispatcher.utter_message(text="It was a tie!")
 
        return []