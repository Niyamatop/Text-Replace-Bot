import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("7187592356:AAEcLMZc_lLffrhpTUXjCSLeeSQUKXzsnyU", "")

    APP_ID = int(os.environ.get("28298365", 12345))

    API_HASH = os.environ.get("9647ab7fc03a8a93f701a5528b2f206e", "")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
