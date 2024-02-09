from dotenv import load_dotenv
import os
import json

# environs kutubxonasidan foydalanish
load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = json.loads(os.getenv("ADMINS"))
IP = os.getenv("ip")
