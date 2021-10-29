from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from database_connectivity import DataUpdate, DataSearch

class ValidateRestaurantForm(Action):
     def name(self) -> Text:
        return "user_details_form"

     def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        required_slot = ["account", "plan"]

        for slot_name in required_slot:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Account=tracker.get_slot("account"),
                                 Plan=tracker.get_slot("plan"))
        DataUpdate(tracker.get_slot("plan"), tracker.get_slot("account"))

class ActionGame(Action):
    def name(self) -> Text:
        return "action_name"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_game",
                                 Game=tracker.get_slot("game"),
                                 Price=DataSearch(tracker.get_slot("game")))