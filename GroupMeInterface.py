import requests



class GroupMeInterface:
    @staticmethod
    def SendMessage(message):
        url = "https://api.groupme.com/v3/bots/post"
        r = requests.post(url, {"text" : message, "bot_id" : "df3e6b7ad8f7f6bc8869a7b051"})

