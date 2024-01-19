 from DAXXMUSIC import app
from os import environ
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest


# Extract environment variables or provide default values
chat_id_env = environ.get("CHAT_ID")
CHAT_ID = [int(app) for app in chat_id_env.split(",")] if chat_id_env else []

TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hᴇʟʟᴏ {mention}\n Wᴇʟᴄᴏᴍᴇ Tᴏ {title}\n\n ")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

