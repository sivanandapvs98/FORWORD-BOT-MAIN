from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import events
import re
from forwardbot.BotConfig import Config
from telethon import errors
from forwardbot import bot
from forwardbot import client
from forwardbot.utils import is_sudo

@bot.on(events.NewMessage(pattern=r'/join'))
async def handler(event):
    if not await is_sudo(event):
        await event.respond("You are not authorized to use this Bot. Create your own.")
        return
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message("Please send the channel invite link as a reply to this message.")
        while True:
            r = conv.wait_event(events.NewMessage(chats=event.chat_id))
            r = await r
            global fromchannel
            link = r.message.message.strip()
            if not r.is_reply:
                await conv.send_message("Please send the message as a reply to the message.")
            else:
                type = ''
                if link:
                    if 't.me/+' in link:
                        chann = re.search(r"t.me/+.(.*)", link)
                        type = 'private'
                    else:
                        chann = re.search(r"t.me.(.*)", link)
                        type = 'public'
                if type == 'private':
                    try:
                        await client(ImportChatInviteRequest(chann.group(1)))
                        await event.respond("Successfully joined the Channel")
                    except errors.UserAlreadyParticipantError:
                        await event.respond("You have already joined the Channel")
                    except:
                        await event.respond("Wrong URL")
                if type == 'public':
                    try:
                        await client(JoinChannelRequest(chann.group(1)))
                        await event.respond("Successfully joined the Channel")
                    except errors.UserAlreadyParticipantError:
                        await event.respond("You have already joined the Channel")
                    except:
                        await event.respond("Wrong URL")

                else:
                    return
                break
