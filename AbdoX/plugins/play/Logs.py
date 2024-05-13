#_____كسمك تحياتي 
#_____@EU_TM

from pyrogram import Client, filters
from AbdoX.core.userbot import Userbot
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_ID
from AbdoX import app


userbot = Userbot()


async def new_message(chat_id: int, message: str, reply_markup=None):
    await app.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        riruru = f"✫ <b><u>جـروب جـديد 🤸‍♂️🖤.</u></b> :\n\nالايدي : {chat_id}\nمعـرف المجموعه : {username}\nالاسـم : {title}\n\nإضـيف بواسطه : {added_by}"
        reply_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            message.from_user.first_name,
            user_id=message.from_user.id
        )
    ]
])

        
        await new_message(LOG_ID, riruru, reply_markup)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "يـوزر غير معروف"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        rirurubye = f"✫ <b><u>غادر جـروب 🥲♥.</u></b> :\n\nالايدي : {chat_id}\nمعـرف المجموعه : {username}\nالاسـم : {title}\n\nطـرد بواسـطه : {remove_by}"
        reply_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            message.from_user.first_name,
            user_id=message.from_user.id
        )
    ]
])

        
        await new_message(LOG_ID, rirurubye, reply_markup)
        await userbot.one.start()
        await userbot.one.leave_chat(chat_id)
