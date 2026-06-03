from pyrogram import filters
from bot import Bot
from pyrogram.types import Message

@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Bot, message: Message):
    await message.reply_text("Hello! Bot is working!")
