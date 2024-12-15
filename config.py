import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29755134"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "04922af1d83f05367c8781383bdc3665")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6350117077"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ganeshchouhan7877:rdX15xt2odwLpXVEdj@cluster0.8r5un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
