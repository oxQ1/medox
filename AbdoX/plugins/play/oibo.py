import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from AbdoX import app




########################### بوت حذف
@app.on_message(filters.command(["الحذف", "عاوز احذف", "عاوزه احذف"], ""))
async def svksksa(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a6137caa707bdb1247d7c.jpg",
        caption=f"""[خش احذف محدش هيمسك فيك يلا غور فداهية 😂❤](https://t.me/LC6BOT)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اضـغـط لـدخول للـبوت", url=f"https://t.me/d_accubot")
                ]
           ]
        ),
    )
   
   
 ########################### قول  
@app.on_message(filters.command(["قول", "كول"], ""))
def elko(client: Client, message: Message):
    tet = message.text.split(None, 1)[1]
    message.reply(tet) 
    
