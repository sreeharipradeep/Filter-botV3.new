from pyrogram import Client, filters
from config import ADMINS

# /broadcast command for admins only
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to broadcast")

    # Copy the replied message to the same chat
    await message.reply_to_message.copy(message.chat.id)
    await message.reply("✅ Broadcast Done")
