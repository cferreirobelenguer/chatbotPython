from nltk.chat.util import Chat,reflections
from responses import intents as respuestas;
#reflection son correcciones de género cuando el usuario habla y el bot responde
my_reflections= {
    "yo": "tú",
    "mi": "tu",
    "yo estoy": "tu estás",
    
}

def chatear():
    #mensaje inicial
    print("Hola, soy el chatbot de atención al cliente de internet. ¿En qué puedo ayudarle?") #mensaje por defecto
    
    chat = Chat(respuestas,my_reflections)
    chat.converse()
    
if __name__ == "__main__":
    chatear()

chatear()