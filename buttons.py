from pyrogram.types import InlineKeyboardButton

start_buttons = [
    [
        InlineKeyboardButton("👥 Group", url="https://t.me/yourgroup"),
        InlineKeyboardButton("📢 Channel", url="https://t.me/yourchannel")
    ],
    [
        InlineKeyboardButton(
            "➕ Add Me To Your Group",
            url="https://t.me/YourBotUsername?startgroup=true"
        )
    ]
]
