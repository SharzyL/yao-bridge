import asyncio
from telethon import TelegramClient, events

# You can apply for api_id and api_hash at https://my.telegram.org/
api_id = 1234567
api_hash = '0000000000000000000000000'

# a list telegram group id that userbot sync message between
# You can get group id by inviting @get_user_id_bot to the group
chat_ids = [-100000000331, -13409302490] 

loop = asyncio.get_event_loop()

# If you are need a proxy to access Telegram
proxy = ('http', '127.0.0.1', 1080)

client = TelegramClient('sync-bot-session', api_id, api_hash, loop=loop, proxy=proxy)
client.start()

@client.on(events.NewMessage(chats=chat_ids))
async def forward_msg(event):
    from_chat_id = event.chat_id
    for chat_id in chat_ids:
        if chat_id != from_chat_id:
            await event.message.forward_to(chat_id)

loop.run_forever()

