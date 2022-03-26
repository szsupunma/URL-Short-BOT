from pyrogram import filters
from bot.modules.funcs import sz_checks
from bot import sz
import json
import requests

@sz.on_message(filters.command("short"))
@sz_checks
async def shorthere(_, message):
    link = message.text.split(None, 1)[1]
    info=json.loads(requests.get(f'https://api.g99solutions.com/linkshort?url={link}').text)
    shorturl = info['shorturl']
    longurl = info['longurl'] 
    date = info['date']  
    title = info['title']
    await sz.send_message(message.chat.id,f"""
**{title}**

• Shorturl - {shorturl}
• Longurl - {longurl}
• Date - `{date}`

► You can get how many times your link has been visited
Giving this command to @szurlshortbot.

● Command : `/statics {shorturl}`

[API](https://t.me/G99Solutions/319) | [support-Chat](https://t.me/slbotzone)
""")

@sz.on_message(filters.command("statics"))
@sz_checks
async def shorthere(_, message):
    link = message.text.split(None, 1)[1]
    info=json.loads(requests.get(f'https://api.g99solutions.com/linkshort?stats={link}').text)
    shorturl = info['shorturl']
    longurl = info['longurl'] 
    date = info['date']  
    title = info['title']
    statics = info['clicks']
    await sz.send_message(message.chat.id,f"""
**{title}** 📊

• statics - {statics}
• Shorturl - {shorturl}
• Longurl - {longurl}
• Date - `{date}`

[API](https://t.me/G99Solutions/319) | [support-Chat](https://t.me/slbotzone)
""")
