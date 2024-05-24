import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary NLTK data files
nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot, and I am here to help yoy.",]
    ],
    [
        r"how are you?",
        ["I'm good. Thanks for asking. How about you?",]
    ],
    [
        r"sorry(.*)",
        ["It's okay.", "No problem.",]
    ],
    [
        r"I am(.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a great day ahead.",]
    ],
    [
        r"(.*)",
        ["I didn't understand that. Can you rephrase?",]
    ],
]
def chatbot():
    print("Hi, How may I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
