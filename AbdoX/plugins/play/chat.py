import asyncio
from typing import Optional
from random import randint
from pyrogram.types import Message, ChatPrivileges
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from AbdoX.utils.database import *
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from AbdoX import app

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await assistant.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"**No group call Found** {err_msg}")
    return False

@app.on_message(filters.regex("^فتح كول$"))
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "تم تشغيل المكالمه يحب❤")
    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("جاري تشغيل المكالمه يحب❤")
    except ChatAdminRequired:
      try:    
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
            ),
        )
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
        )                              
        await msg.edit_text("تم تشغيل المكالمه يحب❤")
      except:
         await msg.edit_text("خلي البوت معاه صلاحية اضافة مشرفين والتحكم ف المحادثه الصوتيه او خلي حساب المساعد مشرف")
@app.on_message(filters.regex("^قفل كول$"))
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعد")
        return
    msg = await app.send_message(chat_id, "↯︙جاري تعطيل ↫ ⦗ المكالمه المرئية ⦘")
    try:
        if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", group call already ended")
           )
        ):  
           return
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("جاري تعطيل المكالمه يحب❤")
    except Exception as e:
      if "GROUPCALL_FORBIDDEN" in str(e):
       try:    
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
             ),
         )
         if not (
           group_call := (
               await get_group_call(assistant, m, err_msg=", group call already ended")
           )
         ):  
           return
         await assistant.invoke(DiscardGroupCall(call=group_call))
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            ),
         )                              
         await msg.edit_text("تم تعطيل المكالمه يحب❤")
       except:
         await msg.edit_text("خلي البوت معاه صلاحية اضافة مشرفين والتحكم ف المحادثه الصوتيه او خلي حساب المساعد مشرف")

  
@app.on_message(filters.command(["تاك","all"]))
async def everyone(client, message):
  global stopProcess
  try: 
    try:
      sender = await app.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if len(chatQueue) > 5:
        await message.reply("-› I'm already working on my maximum number of 5 chats at the moment. Please try again shortly.")
      else:  
        if message.chat.id in chatQueue:
          await message.reply("-› There's already an ongoing process in this chat. Please /stop to start a new one.")
        else:  
          chatQueue.append(message.chat.id)
          if len(message.command) > 1:
            inputText = " ".join(message.command[1:])
          elif len(message.command) == 1:
            inputText = ""    
          membersList = []
          async for member in app.get_chat_members(message.chat.id):
            if member.user.is_bot == True:
              pass
            elif member.user.is_deleted == True:
              pass
            else:
              membersList.append(member.user)
          i = 0
          lenMembersList = len(membersList)
          if stopProcess: stopProcess = False
          while len(membersList) > 0 and not stopProcess :
            j = 0
            text1 = f"{inputText}\n\n"
            try:    
              while j < 10:
                user = membersList.pop(0)
                if user.username == None:
                  text1 += f"{user.mention} "
                  j+=1
                else:
                  text1 += f"@{user.username} "
                  j+=1
              try:     
                await app.send_message(message.chat.id, text1)
              except Exception:
                pass  
              await asyncio.sleep(1) 
              i+=10
            except IndexError:
              try:
                await app.send_message(message.chat.id, text1)  
              except Exception:
                pass  
              i = i+j
          if i == lenMembersList:    
            await message.reply(f"-› Successfully mentioned total number of {i} members.\n-› Bots and deleted accounts were rejected.") 
          else:
            await message.reply(f"-› Successfully mentioned {i} members.\n-› Bots and deleted accounts were rejected.")    
          chatQueue.remove(message.chat.id)
    else:
      await message.reply("-› Sorry, only admins can execute this command.")  
  except FloodWait as e:
    await asyncio.sleep(e.value)                    
        
@app.on_message(filters.command(["stop","cancel"]))
async def stop(client, message):
  global stopProcess
  try:
    try:
      sender = await app.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if not message.chat.id in chatQueue:
        await message.reply("-› There is no ongoing process to stop.")
      else:
        stopProcess = True
        await message.reply("-› Stopped.")
    else:
      await message.reply("-› Sorry, only admins can execute this command.")
  except FloodWait as e:
    await asyncio.sleep(e.value)

print("[✓]  Your client has been started ")
