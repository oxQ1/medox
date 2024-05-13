#_____كسمك تحياتي 
#_____@EU_TM


from pyrogram import Client, filters
from pyrogram.types import Message
from AbdoX import app

@app.on_message(filters.command("كشف مجموعه", prefixes=""))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("الرجاء تقديم اسم مستخدم المجموعة. مثال:كشف مجموعه @EU_TM")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"➖➖➖➖➖➖➖\n"
        f"↝ أسم المجموعة : {group.title} ✅\n"
        f"↝ معرف مجموعة : {group.id}\n"
        f"↝ إجمالي الأعضاء : {total_members}\n"
        f"↝ البايو : {group_description or 'N/A'}\n"
        f"↝ اليوزر : {group_username}\n"
       
        f"➖➖➖➖➖➖➖"
    )
    
    await message.reply(response_text)

@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat
    status_text = f"Group ID: {chat.id}\n" \
                  f"Title: {chat.title}\n" \
                  f"Type: {chat.type}\n"
                  
    if chat.username:
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)
