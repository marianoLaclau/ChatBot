from typing import Any, Text, Dict, List
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProveerInformacion(Action):

    def name(self) -> Text:
        return "action_proveer_informacion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Puedo brindarte información sobre nuestros sevicios.")
        return []


class ActionProveerHora(Action):

    def name(self) -> Text:
        return "action_proveer_hora"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        dispatcher.utter_message(text=f"La hora actual es {current_time}.")
        return []


class ActionProveerDia(Action):

    def name(self) -> Text:
        return "action_proveer_dia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Obtener el día actual en inglés
        now = datetime.now()
        current_day = now.strftime("%A, %d de %B de %Y")

        # Diccionarios para traducir días y meses
        days_translation = {
            "Monday": "Lunes",
            "Tuesday": "Martes",
            "Wednesday": "Miércoles",
            "Thursday": "Jueves",
            "Friday": "Viernes",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }
        
        months_translation = {
            "January": "Enero",
            "February": "Febrero",
            "March": "Marzo",
            "April": "Abril",
            "May": "Mayo",
            "June": "Junio",
            "July": "Julio",
            "August": "Agosto",
            "September": "Septiembre",
            "October": "Octubre",
            "November": "Noviembre",
            "December": "Diciembre"
        }

        # Traducir día y mes
        for en, es in days_translation.items():
            current_day = current_day.replace(en, es)
        
        for en, es in months_translation.items():
            current_day = current_day.replace(en, es)

        # Enviar la respuesta al usuario
        dispatcher.utter_message(text=f"Hoy es {current_day}.")
        return []


class ActionProveerClima(Action):

    def name(self) -> Text:
        return "action_proveer_clima"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ubicacion = tracker.get_slot('ubicacion')
        dispatcher.utter_message(text=f"El clima en {ubicacion} es soleado.")  # Aquí podrías integrar con una API de clima
        return []
    

