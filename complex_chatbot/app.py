from flask import Flask, render_template, request, jsonify
import random
import json
import os
import re

# Define initial training data and responses
training_data = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey!"]
    },
    "name": {
        "patterns": ["what is your name", "who are you"],
        "responses": ["I am a chatbot, here to assist you."]
    },
    "how_are_you": {
        "patterns": ["how are you", "how are you doing"],
        "responses": ["I'm just a bunch of code, but I'm functioning as expected!"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later"],
        "responses": ["Bye! Take care.", "Goodbye! Have a great day ahead."]
    },
    "special_pattern": {
        "patterns": ["How's it going?", "What's up?", "What's new?"],
        "responses": ["I'm doing well, thank you!", 'Not much, just chatting with you!']
    },
    "fallback": {
        "patterns": [".*"],
        "responses": ["I didn't understand that. Can you rephrase?", "Sorry, I didn't get that."]
    }
}

# Load existing training data if available
if os.path.exists("training_data.json"):
    with open("training_data.json", "r") as file:
        training_data.update(json.load(file))
print(training_data)
# Function to save training data
def save_training_data():
    with open("training_data.json", "w") as file:
        json.dump(training_data, file)


def get_response(text):
    for intent, data in training_data.items():
        for pattern in data["patterns"]:
            print(pattern,text)
            if re.search(pattern, text, re.IGNORECASE):
                return random.choice(data["responses"])
    return random.choice(training_data["fallback"]["responses"])

def learn_statement(statement, response):
    # Check if the intent already exists
    for intent, data in training_data.items():
        if statement in data["patterns"]:
            training_data[intent]["responses"].append(response)
            break
    else:
        # Create a new intent if not found
        update_dict = {statement:{
            "patterns": [statement],
            "responses": [response]
        }}
        not_found_res = training_data.pop("fallback")
        training_data.update(update_dict)
        popped_dict = {"fallback":not_found_res}
        training_data.update(popped_dict)
    save_training_data()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_chatbot_response():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

@app.route("/learn", methods=["POST"])
def learn():
    statement = request.json.get("statement")
    response = request.json.get("response")
    learn_statement(statement.strip(), response.strip())
    return jsonify({"response": "Learned: '{}' -> '{}'".format(statement, response)})

if __name__ == "__main__":
    app.run(debug=True)
