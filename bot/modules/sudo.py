from bot import sz, SUDO_ID as SUDO
from pyrogram import filters
from bot.modules.sql import count_users, user_list, remove_user

me = '1467358214'

@sz.on_message(filters.command("stats") & filters.user(me))
async def botsatats(_, message):
    users = count_users()
    await message.reply_text(f"Total Users -  {users}")


@sz.on_message(filters.command('bcast') & filters.user(SUDO))
async def broadcast(_, message):
    if message.reply_to_message :
        await message.reply_text("Started broadcast")
        query = user_list()
        for row in query:
           try: 
            chat_id = int(row[0])
            reply = message.reply_to_message
            await reply.copy(chat_id)
           except:
            pass
            remove_user(chat_id)
            await message.reply_text(f"{chat_id} blocked me, Removed from DB.")
