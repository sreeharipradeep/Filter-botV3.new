from pyrogram import Client, filters

# /help command handler
@Client.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message):
    await message.reply_text("""
📌 Commands

/start - Start bot
/filter - Add movie filter
/broadcast - Admin broadcast
/help - Help
""")
