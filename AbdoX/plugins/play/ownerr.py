import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from AbdoX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(filters.command(["المطور","مطور "], ""))
async def khfzss(client: Client, message: Message):
    usrr = await client.get_chat(OWNER_ID)
    name = usrr.first_name
    bio = usrr.bio
    id = usrr.id
    username = usrr.username
    async for photo in client.get_chat_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""مــعلومــات مــطور الــبـوت : \n\n name: {name} \n\n usre: @{username} \n\n id: {id} \n\n bio: {bio} \n\n 𝐒𝐎𝐔𝐑𝐂𝐄 𝐁𝐎𝐃𝐀""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{username}")
                ],
            ]
        ),
    )                    
                    

                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}\n\n مجموعه : {chatusername}")
                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}\n\n مجموعه: {chatusername}")

@app.on_message(filters.command(["تحويل لصوره"], ""))
async def elkatifh(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



