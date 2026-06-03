from pyrogram import filters
from pyrogram.types import Message

def register(app):
    @app.on_message(filters.command('start') & filters.private)
    async def start_command(client, message: Message):
        await message.reply_text("**Hello! Bot is working!** ✅")
