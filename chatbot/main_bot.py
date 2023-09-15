from chatterbot import ChatBot
import spacy
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os



# spacy.cli.download("en_core_web_sm")
# spacy.cli.download("en_core_web_md")
# spacy.cli.download("en")

# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en_core_web_md')

chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.80
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
trainer = ListTrainer(chatbot)


# Get the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the paths to the data files
training_data_quesans_path = os.path.join(BASE_DIR, 'training_data', 'ques_ans.txt')
training_data_personal_path = os.path.join(BASE_DIR, 'training_data', 'personal_ques.txt')

# Open and read the data files
training_data_quesans = open(training_data_quesans_path).read().splitlines()
training_data_personal = open(training_data_personal_path).read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

# Training With Corpus
trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)