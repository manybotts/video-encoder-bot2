import os
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = os.environ.get("API_ID", 5166878)
api_hash = os.environ.get("API_HASH", "fdafb41f9a67f40e34a6c67f47730a92")
bot_token = os.environ.get("BOT_TOKEN", "5870372680:AAENb7lbqL1oFyP2KCQRD3TJQ8Zr-ro2AE8")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = os.environ.get("SUDO_USERS", 762308466)

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
