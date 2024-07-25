from typing import Any, Text, Dict, List
from datetime import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests



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

        api_key = "806dd52b94a3bb14b5345bb4ac8a7497"  # Reemplaza esto con tu API Key de OpenWeatherMap
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Obtener la ubicación del slot
        ubicacion = tracker.get_slot('ubicacion')
        
        if ubicacion is None:
            dispatcher.utter_message(text="No he podido obtener la ubicación. ¿Puedes repetirla, por favor?")
            return []

        # Construir la URL completa para la solicitud
        complete_url = f"{base_url}?q={ubicacion}&appid={api_key}&units=metric&lang=es"
        
        # Hacer la solicitud a la API
        response = requests.get(complete_url)
        data = response.json()
        
        # Verificar si se ha encontrado la ciudad
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperatura = main["temp"]
            descripcion = weather["description"]
            ubicacion = ubicacion.title()
            dispatcher.utter_message(text=f"El clima en {ubicacion} es: {descripcion}, con una temperatura de {temperatura}°C.")
        else:
            dispatcher.utter_message(text=f"No he podido encontrar el clima para la ubicación: {ubicacion}. Por favor, verifica el nombre de la ciudad.")
        
        return []
    

