from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply("""
📌 Commands

/start - Start bot
/filter - Add movie filter
/broadcast - Admin broadcast
/help - Help
""")
