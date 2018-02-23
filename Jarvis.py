from GroupMeInterface import GroupMeInterface


class Jarvis:
    def __init__(self, logger):
        self.talkingTo = None
        self.logger = logger

    def ParseAndRespond(self, incoming):
        incoming = incoming
        body = incoming["text"].lower()
        self.logger.debug("Body: " + body)

        speaker = incoming["name"]
        self.logger.debug("Speaker: " + speaker)

        if body.startswith("jarvis"):
            self.Acknowledge(speaker)

        if speaker == self.talkingTo:
            if body == "thanks" or body == "thx":
                self.EndConversation()

    def Acknowledge(self, name):
        self.logger.debug("In Acknowledge")
        self.talkingTo = name
        self.Speak("How can I help you, " + self.talkingTo + "?")

    def EndConversation(self):
        self.logger.debug("In EndConversation")
        self.talkingTo = None
        self.Speak("You're welcome")

    def Speak(self, text):
        GroupMeInterface.SendMessage(text)

