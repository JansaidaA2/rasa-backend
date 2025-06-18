from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionScheduleBooking(Action):
    def name(self) -> str:
        return "action_schedule_booking"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: dict):
        # Your logic here
        dispatcher.utter_message(text="Your booking has been scheduled.")
        return []
