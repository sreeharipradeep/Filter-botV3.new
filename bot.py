from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "MovieFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

from handlers import start, filter, broadcast, help

app.run()
