from fuzzywuzzy import fuzz
import re
from  speech import TextToSpeechPrinter
class ChatBot:
    def __init__(self):
        self.name = "NormalPerson"
        self.name_name = "User"

    def save_user_name(self, user_name):
        self.user_name = user_name

    def get_user_info(self):
        print("What is your name? ")
        name=input(f"{self.user_name}")
        self.save_user_name(name)
        print(f"Welcome {self.user_name}")

    def get_response(self, user_input):
        fuzzy_match_threshold = 70 # can change this if needed

        # Define our input phrases with their answers
        predefined_inputs = {
            "Hello": f"Hello There {self.username}!",
            "How are you?": "Doing as awesome as I can be.",
            "Who are you?":f"My name is {self.name}",
            "How do you convince people?": "I talk to people as would a normal person!",
            "You ever wonder why we're here?": "That's one of life's greatest mysteries isn't it. Why are we here?",
        }

        # Tokenize the user input
        user_input_tokens = re.findall(r'\w+' ,user_input.lower())

        best_match = None
        best_match_ratio = 0

        for input_phrase in predefined_inputs:
            # tokenize the predefined input keys
            input_phrase_tokens = re.findall(r'\w+' ,user_input.lower())

            match_ratio = fuzz.partial_ratio(user_input_tokens, input_phrase_tokens)

            if match_ratio > best_match_ratio:
                best_match = input_phrase
                best_match_ratio = match_ratio

        # Generate our Response based on the based match
        if best_match and best_match_ratio >= fuzzy_match_threshold:
            return predefined_inputs[best_match]
        else:
            return "English? Do you speak it?"

    def start_chat(self):
        print("Welcome! I'm {self.name}")
        self.get_user_info()
        print("What can I so for you today?")
        
        while True:
            user_input = input(f"{self.user_name}:")
            if user_input.lower() == "quit":
                print("Bye! We will see each other again!")
                break

            response = self.get_response(user_input)
            print(response)
            
with TextToSpeechPrinter: 
    chatbot = ChatBot()
    chatbot.start_chat()            