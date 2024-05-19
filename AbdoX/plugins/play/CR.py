#_____كسمك تحياتي 
#_____@EU_TM

import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from AbdoX import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b56c2f4ff37d1f22dd38a.jpg",
        caption=f"𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐬𝐨𝐮𝐫𝐜𝐞 𝐦𝐞𝐝𝐨 𝐚𝐥𝐞𝐱 ၄",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/U7_4K"), 
                 InlineKeyboardButton(
                   " 𝐒𝐎𝐔𝐑𝐂𝐄",       url=f"https://t.me/UJ_5Q"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "˛𝑴𝑬𝑫𝑶 𓏺 𝑨𝑳𝑬𝑿 ᭡ٰ🇵🇸💤 ", url=f"https://t.me/ox_Q1"), 
                   InlineKeyboardButton(
                        " [ 𝑬𝑯𝑨𝑨𝑩 𝒁𝑨3𝑬𝑴 ]الـمتـوحـد  ", url=f"https://t.me/EHepp"), 
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("ox_Q1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس\n\n‍ ¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\𝐒𝐎𝐔𝐑𝐂𝐄 𝐌𝐄𝐃𝐎 𖠱", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["ميدو"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("ox_Q1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"مــعلومـات مــطور الـسـورس \n\n dev :{name}\n\n user :@{usr.username}\n\n id :`{usr.id}`\n\n boi :{usr.bio}\n\n 𝐒𝐎𝐔𝐑𝐂𝐄 𝐌𝐄𝐃𝐎 𖠱", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



@app.on_message(
    command(["مبرمج السورس" , "مودي","السفل"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("VIP_lD")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"مــعلـومـات مــبرمـج الـسـورس  \n\n dev :{name}\n\n user :@{usr.username}\n\n id :`{usr.id}`\n\n bio :{usr.bio}\n\n𝐒𝐎𝐔𝐑𝐂𝐄 𝐌𝐄𝐃𝐎 𖠱", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
                  )
