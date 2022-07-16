# @supunma
from pyrogram import Client
from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
SQL_DB = getenv("SQL_DB")
SUDO_ID = getenv("SUDO_ID")

sz = Client("Bot", 
            bot_token=BOT_TOKEN, 
            api_hash=API_HASH, 
            api_id=API_ID)
