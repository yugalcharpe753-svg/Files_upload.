# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8545421376:AAFzFdh_7_sywo7_KbiJ29gYKux4ALBckCA")
APP_ID = int(os.environ.get("APP_ID", "29780235"))
API_HASH = os.environ.get("API_HASH", "5d3404de54587fb6eec7f1aef656018d")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003675100602"))
OWNER = os.environ.get("OWNER", "SANATANI_B0Y")
OWNER_ID = int(os.environ.get("OWNER_ID", "6275020364"))

PORT = os.environ.get("PORT", "8001")
BASE_URL = os.environ.get("BASE_URL", "https://file-bot-pgv0.onrender.com")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://FilestoreDB:Darkauli%401234@infinityfile.pitecuw.mongodb.net/?appName=Infinityfile")
DB_NAME = os.environ.get("DATABASE_NAME", "FilestoreDB")

FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/R0Y4L_KING")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/FkgGQYby/welcome.png")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/FkgGQYby/welcome.png")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "https://shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "0fbaf68e49013099204197ba4ed03a01c7196386")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/H0W_2_USE/12")
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"
SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")

HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @ModAppsKing\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/ModAppsKing>ᴍᴏᴅᴀᴘᴘsᴋɪɴɢ</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/ModAppsKing>ModAppsKing</a>\n◈ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+i6NIEXiiQWM2YTll>ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ</a>\n◈ ᴇᴅᴜ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/EduAppsKing>EduAppsKing</a>\n◈ ᴄᴏᴜʀsᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/FATHER_OF_COURSE>Father Of Course</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ : <a href=https://t.me/R0Y4L_KING>R0Y4L_KING</a></blockquote></b>"

START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b><blockquote>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b></blockquote>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /addpremium :</b> ᴀᴅᴅ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
"""

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @ModAppsKing</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "😂 Bhai seedha baat mat kar, /start dabao!"

OWNER_TAG = os.environ.get("OWNER_TAG", "R0Y4L_KING")
UPI_ID = os.environ.get("UPI_ID", "20213904@axl")
QR_PIC = os.environ.get("QR_PIC", "https://i.ibb.co/35QF8QMJ/QR.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "t.me/R0Y4L_KING")

PRICE1 = os.environ.get("PRICE1", "0 rs")
PRICE2 = os.environ.get("PRICE2", "60 rs")
PRICE3 = os.environ.get("PRICE3", "150 rs")
PRICE4 = os.environ.get("PRICE4", "280 rs")
PRICE5 = os.environ.get("PRICE5", "550 rs")

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
