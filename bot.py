from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Initialize Pyrogram Client
app = Client(
    "MovieFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Import command handlers
import start
import filter
import broadcast
import help

# Run the bot
app.run()
