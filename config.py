# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20136640"
    API_HASH = "32fa482ffd34ceefec26b7ccd73c4fbb"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7324432991:AAF2GaYhLNqHWz3aIzC3EnoE16BG0OiZvMA")
    MONGO_URL = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/73cd2c73ff6d19923774c.jpg"
    SUDOERS = filters.user(["7548614955"])
