from pyrogram import Client, filters
from database.filters import add_filter, get_filter

@Client.on_message(filters.command("filter") & filters.reply)
async def add_filter_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /filter movie_name")

    keyword = message.command[1].lower()
    replied = message.reply_to_message

    if replied.video:
        file_id = replied.video.file_id
    elif replied.document:
        file_id = replied.document.file_id
    else:
        return await message.reply("Reply to a file or video")

    add_filter(keyword, file_id)
    await message.reply("✅ Filter added")

@Client.on_message(filters.text & filters.group)
async def auto_filter(client, message):
    data = get_filter(message.text.lower())
    if data:
        await client.send_cached_media(
            chat_id=message.chat.id,
            file_id=data["file_id"],
            reply_to_message_id=message.id
        )
