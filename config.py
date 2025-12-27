import os

# Telegram API credentials
API_ID = int(os.environ.get("API_ID", "36360287"))
API_HASH = os.environ.get("API_HASH", "4283a743d393b1094600a7065a50b3c0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8518993193:AAE1OVHCiOka97i9KXC18RNJkIxD0uPe-I8")

# MongoDB connection URL
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://Mreldro:mreldro@cluster0.wdjsw5c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Bot admins (your Telegram ID)
ADMINS = [8417661273]
