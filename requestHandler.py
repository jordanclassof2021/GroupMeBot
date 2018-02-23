from Jarvis import Jarvis
import os, logging
from flask import Flask, request, json

app = Flask(__name__)
jarvis = Jarvis(app.logger)
app.debug = True


#jarvis.Speak("Celtics & Rockets are the best teams in the NBA")

bestrappers = ["Kendrick","Naz","Jay-Z","2Pac"]

for rapper in bestrappers:
    blurb = "I like %s" % rapper
    jarvis.Speak(blurb)

@app.route('/', methods=['POST'])
def requestHandler():
    incoming = request.get_json(force=True)
    app.logger.debug(incoming)
    if incoming["name"] != "Jarvis":
        jarvis.ParseAndRespond(incoming)

    return ""

