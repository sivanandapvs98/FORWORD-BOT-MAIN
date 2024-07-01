from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "29868868")
    API_HASH = environ.get("API_HASH", "6b7bd10846ff6d7e8f50a4bfe13c9fd4")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7014461118:AAESAgPjfHgMwK6tEyCqWPuiQK1kgvUuGXY")
    STRING_SESSION = environ.get("STRING_SESSION", "1BVtsOHcBu5Q88zlHBcGYdIlDF7-V66t6eNegXnsYpxcs8P1LHfyMCR8dsKayGnm79TTxlftCfxGeWOlZi60Ku-rgwaNT2YjQnTox1GjXPk6iFujJvO1d80wq-bE9ozNv2s2UJNj3HX2AHwNl5krO3xgv0Y8AOesaJu0Gw8CjHesaEQ0Z4a2IbIqaJ3Lzcp_cg83vYGA2aUSxK-PaCS5PLhUq0d3Bn0F9CCmMY49d3HX9XcvYhJjlFvLrIKn8tWZhBf9K0bH0bfspumJwZM5yokL8T1CqTTGim9Yolm1VvJiPWyA8UwW4VDaRSmQ13Eje4NchrBdjdlvytzlq-nCrNME8ezSGNzg=")
    SUDO_USERS = environ.get("SUDO_USERS", "1408595569 786843013 5884953489")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@uniqueuser7410**
    """
