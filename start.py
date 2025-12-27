from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from buttons import start_buttons  # Ensure buttons.py root-level-layirikkanam

# Welcome message
WELCOME_TEXT = """🍿 Welcome! 🍿

I am the filter bot of the Trixel Movie group 🎬.
You can add me to your channel or group and use me.

🍿 സ്വാഗതം! 🍿

ഞാൻ Trixel Movie 🎬 ഗ്രൂപ്പിന്റെ ഫിൽട്ടർ ബോട്ട് ആണ്.
നിങ്ങൾ എന്നെ നിങ്ങളുടെ Channel / Group-ൽ add ചെയ്ത്
use ചെയ്യാവുന്നതാണ് ☺️
"""

# /start command handler
@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://graph.org/file/62386b57bf0394d7bd917-959daf5976f788890f.jpg",
        caption=WELCOME_TEXT,
        reply_markup=InlineKeyboardMarkup(start_buttons)
    )
