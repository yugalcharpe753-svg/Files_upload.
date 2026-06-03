
# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aiohttp import web
from plugins.web_server import web_server
import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
import pytz
from datetime import datetime
#rohit_1888 on Tg
from config import *
from db_premium import *
from database import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

# Suppress APScheduler logs below WARNING level
logging.getLogger("apscheduler").setLevel(logging.WARNING)

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(remove_expired_users, "interval", seconds=10)

# Reset verify count for all users daily at 00:00 IST
async def daily_reset_task():
    try:
        await db.reset_all_verify_counts()
    except Exception:
        pass  

scheduler.add_job(daily_reset_task, "cron", hour=0, minute=0)
#scheduler.start()


def get_indian_time():
    """Returns the current time in IST."""
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist)


name ="""
 BY CODEFLIX BOTS
"""

def get_indian_time():
    """Returns the current time in IST."""
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        scheduler.start()
        usr_bot_me = await self.get_me()
        self.uptime = get_indian_time()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            print(f"CHANNEL ERROR: {e}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
            #sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(rf"Bot Running..!\n\nCreated by \nhttps://t.me/weebs_support")
        self.LOGGER(__name__).info(f"""       


  ___ ___  ___  ___ ___ _    _____  _____  ___ _____ ___ 
 / __/ _ \|   \| __| __| |  |_ _\ \/ / _ )/ _ \_   _/ __|
| (_| (_) | |) | _|| _|| |__ | | >  <| _ \ (_) || | \__ \
 \___\___/|___/|___|_| |____|___/_/\_\___/\___/ |_| |___/
                                                         
 
                                          """)

        self.set_parse_mode(ParseMode.HTML)
        self.username = usr_bot_me.username
        self.LOGGER(__name__).info(f"Bot Running..! Made by @Codeflix_Bots")   

        # Start Web Server
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()


        try: await self.send_message(OWNER_ID, text = f"<b><blockquote> Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ by @Entertainmen9</blockquote></b>")
        except: pass

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    def run(self):
        """Run the bot."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.start())
        self.LOGGER(__name__).info("Bot is now running. Thanks to @King")
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            self.LOGGER(__name__).info("Shutting down...")
        finally:
            loop.run_until_complete(self.stop())

#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
