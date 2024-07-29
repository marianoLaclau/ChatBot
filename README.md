# ChatBot NLP Experimental Creado con Rasa
Este es un proyecto experimental de ChatBot basado en Procesamiento de Lenguaje Natural (NLP) creado con Rasa. El objetivo de este chatbot es proporcionar respuestas naturales y contextuales a las consultas de los usuarios, y puede ser adaptado para diferentes empresas y servicios.

## Características
* Respuestas predefinidas para preguntas comunes.
* Capacidad de extraer entidades como nombres, ubicaciones y fechas.
* Acciones personalizadas para proporcionar información adicional como el clima actual.
* Soporte para respuestas variadas para hacer las interacciones más naturales.


## Requisitos
* Python 3.9
* Rasa 3.1.0
* OpenWeatherMap API Key para el servicio de clima


## Instalación
### Clona el repositorio:

git clone https://github.com/marianoLaclau/ChatBot.git

cd ChatBot

### Crea un entorno virtual:

python3.9 -m venv rasa_env

source rasa_env/bin/activate  
En Windows: rasa_env\Scripts\activate

### Instala las dependencias:

pip install -r requirements.txt

### Configura tu API Key de OpenWeatherMap en el archivo actions.py.


## Archivos del Proyecto
* domain.yml: Define las intenciones, entidades, acciones y respuestas predefinidas del bot.
* nlu.yml: Contiene los ejemplos de entrenamiento para las diferentes intenciones que el bot puede reconocer.
* stories.yml: Ejemplos de historias que representan posibles conversaciones con el bot.
* rules.yml: Reglas específicas para manejar ciertos patrones de conversación.
* actions.py: Contiene las acciones personalizadas que el bot puede ejecutar.
* config.yml: Configuración del pipeline de procesamiento de lenguaje natural.
* endpoints.yml: Configuración de los endpoints para acciones personalizadas y otros servicios.


## Uso
### Entrena el modelo de Rasa:

rasa train

### Inicia el servidor de acciones:

rasa run actions

### Inicia el chatbot:

rasa shell


## Ejemplos de Interacción
**Usuario:** hola

**Bot:** ¡Hola! ¿Cómo puedo ayudarte hoy?

**Usuario:** me llamo Mariano

**Bot:** Hola Mariano, ¿en qué puedo ayudarte?

**Usuario:** ¿cómo está el clima en Buenos Aires?

**Bot:** El clima en Buenos Aires es 20°C con cielo despejado.

**Usuario:** gracias

**Bot:** ¡De nada! ¿Hay algo más en lo que pueda ayudarte?

**Usuario:** adiós

**Bot:** ¡Adiós! ¡Que tengas un buen día!


