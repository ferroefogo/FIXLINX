import os
from dotenv.main import load_dotenv

load_dotenv()

BOT_NAME = "FIXLINX"
BOT_TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD_ID")