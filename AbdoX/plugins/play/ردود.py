import asyncio
import random
from AbdoX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import filters, Client




@app.on_message(filters.text, group=39)
async def almortagel(client, message):
   if message.text == "😒":
       await message.reply_text(f"عدل وشك ونت بتكلمني 😒🙄")
   elif message.text == "💋":
       await message.reply_text(f" نا عايز مح انا كمان 🥺💔")
   elif message.text ==  "😭":
       await message.reply_text(f"بتعيط تيب لي طيب 😥")
   elif message.text == "🥺":
       await message.reply_text(f"متزعلش بحبك 😻🤍")
   elif message.text == "😂":
       await message.reply_text(f"ضحكتك عثل زيكك ينوحيي 🌝❤️")
   elif message.text == "🤔":
       await message.reply_text(f"بتفكر في اي 🤔")
   elif message.text == "🌚":
       await message.reply_text(f"القمر ده شبهك 🙂❤️")
   elif message.text == "نعم":
       await message.reply_text(f" نعم الله عليك 🌚❤️")
   elif "." in message.text:
       await message.reply_text(f"صلي علي النبي وتبسم ✨♥")
   elif message.text == "سلام":
       await message.reply_text(f" مع الف سلامه يقلبي متجيش تاني 😹💔🎶")
   elif message.text == "🙄":
       await message.reply_text(f" نزل عينك تحت كدا علشان هتخاد علي قفاك 😒❤️")
   elif message.text == "برايفت":
       await message.reply_text(f"خدوني معاكم برايفت والنبي 🥺💔")
   elif message.text == "بف":
       await message.reply_text(f"خدوني معاكم بف والنبي 🥺💔")
   elif message.text == "السلام عليكم":
       await message.reply_text(f"وعليكم السلام 🌝💜")
   elif message.text == "هاي":
       await message.reply_text(f"هآي تع اشب شااي • 😹💔")        
   elif message.text == "محح":
       await message.reply_text(f" محات حياتي يروحي 🌝❤️")
   elif message.text == "بحبك":
       await message.reply_text(f"وانا كمان بعشقك يا روحي 🤗🥰")
   elif message.text == "الحمدلله":
       await message.reply_text(f"دايما ياحبيبي 🌝❤️")
   elif message.text == "هشش":
       await message.reply_text(f" بنهش كتاكيت احنا هنا ولا اي ??😹")        
   elif message.text == "هلا":
       await message.reply_text(f" هلا بيك ياروحي 👋")
   elif message.text == "بف":
       await message.reply_text(f"وحيات امك ياكبتن خدوني معاكو بيف 🥺💔")
   elif message.text == "خاص":
       await message.reply_text(f"ونجيب اشخاص 😂👻")
   elif message.text == "بخير":
       await message.reply_text(f"انت الخير يعمري 🌝❤️")        
   elif message.text == "اه":
       await message.reply_text(f" اه اي يا قدع عيب 😹💔")
   elif message.text == "حصل":
       await message.reply_text(f"خخخ امال 😹")        
   elif message.text == "تع":
       await message.reply_text(f"لا عيب بتكسف 😹💔")
   elif message.text == "منور":
       await message.reply_text(f" ده نورك ي قلبي 🌝💙")        
   elif message.text == "ويت":
       await message.reply_text(f" اي الثقافه دي 😒😹")
   elif message.text == "خخخ":
       await message.reply_text(f" اهدا يوحش ميصحش كدا 😒?")        
   elif message.text == "باي":
       await message.reply_text(f"ع فين لوين رايح وسايبنى 🥺💔")
   elif message.text == "شكرا":
       await message.reply_text(f"العفو ياروحي 🙈🌝")        
   elif message.text == "حلوه":
       await message.reply_text(f" انت الي حلو ياقمر 🤤🌝")
   elif message.text == "بموت":
       await message.reply_text(f"موت بعيد م ناقصين مصايب 😑😂")        
   elif message.text == "تيب":
       await message.reply_text(f"فرح خالتك قريب 😹💋💃🏻")
   elif message.text == "اي":
       await message.reply_text(f"جتك اوهه م سامع ولا ايي 😹👻")        
   elif message.text == "حاضر":
       await message.reply_text(f"حضرلك الخير يارب 🙂❤️")
   elif message.text == "سي في":
       await message.reply_text(f"كفيه شقط سيب حاجه لغيرك 😎😂")        
   elif message.text == "جيت":
       await message.reply_text(f"لف ورجع تانى مشحوار 😂🚶‍♂👻")
   elif message.text == "بخ":
       await message.reply_text(f"يوه خضتني ياسمك اي 🥺💔")        
   elif message.text == "خلاص":
       await message.reply_text(f"خلصتت روحكك يبعيد 😹💔")
   elif message.text == "حبيبي":
       await message.reply_text(f"اوه ياه 🌝😂")
   elif message.text == "تمام":
       await message.reply_text(f"امك اسمها احلام 😹😹")