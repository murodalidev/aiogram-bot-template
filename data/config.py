from dotenv import load_dotenv
import os
import json

# environs kutubxonasidan foydalanish
load_dotenv()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Bot token
ADMINS = json.loads(os.environ.get("ADMINS"))  # adminlar ro'yxati
IP = os.environ.get("ip")  # Xosting ip manzili
