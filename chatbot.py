# Importar chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Nombrar al chatbot
chatbot = ChatBot(
    name = 'Jarvis',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation',
    ],
    database_uri = 'sqlite:///database.sqlite3'
)

# Entrenar al chatbor
conversation = [
    "Hello. How can I help you?",
    "I would like to book a flight",
    "What date would you like to flight?",
    "On Spring Break",
    "What would be your destiny?",
    "Merida, Yucatan",
    "Your flight has been booked",
]

tariner = ListTrainer(chatbot)
tariner.train(conversation)

# loop para hablar con el chatbot
userName = input("Enter your name: ")
print("Welcome to the chat. How can I help you?")

while True:
    request = input(f"{userName}: ")

    if request == 'Bye' or request == 'bye':
        print(f"{chatbot.name}: Bye")
        break
    else:
        response = chatbot.get_response(request)
        print(f"{chatbot.name}: {response}")
