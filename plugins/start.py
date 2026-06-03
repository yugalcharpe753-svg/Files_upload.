from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from config import *
from helper_func import *
from database import *

@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Bot, message: Message):
    await message.reply_text(
        text=START_MSG.format(
    mention=message.from_user.mention
),
        disable_web_page_preview=True
    )
