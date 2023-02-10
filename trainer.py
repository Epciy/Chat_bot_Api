from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_random_response
import os


chatbot = ChatBot(
    'ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #'mysql://user:password@localhost/dbname'
    database_uri='mysql://root:root@localhost/chat_dash',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            
            "statement_comparison_function": LevenshteinDistance,
            "response_selection_method": get_random_response,
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
        
    ],)



path = "./knowledge"
files =set()
def get_files(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) and filename not in files:
            files.add(path+"/"+filename)
    return files

trainer = ChatterBotCorpusTrainer(chatbot)


for file in get_files(path):
    trainer.train(file)

# Start the chatbot
def brain(user_input):
    response=chatbot.get_response(user_input)
    return response
