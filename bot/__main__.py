from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from bot.modules.sql import add_user
from bot.modules.funcs import sz_checks
from bot.modules import *
from bot import sz
from bot.modules.sql import count_users

keyboard = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton(text="Support Group", url=f"https://t.me/slbotzone"),
    ]]
)

@sz.on_message(filters.command("start"))
@sz_checks
async def startmsg(_, message):
    users = count_users() 
    START_TEXT = f"""
Hello !

URL-Short-BOT can short your long URL in seconds, It also lets you know how many times your link has been visited !

• **Total Users** : `{users}`
[API](https://t.me/G99Solutions/319) | [support-Chat](https://t.me/slbotzone)
"""
    await sz.send_message(message.chat.id, START_TEXT,disable_web_page_preview=True, reply_markup=keyboard)
    add_user(message.from_user.id, message.from_user.first_name)

sz.run()
