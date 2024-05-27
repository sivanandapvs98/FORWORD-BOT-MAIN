from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "29868868")
    API_HASH = environ.get("API_HASH", "6b7bd10846ff6d7e8f50a4bfe13c9fd4")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7014461118:AAESAgPjfHgMwK6tEyCqWPuiQK1kgvUuGXY")
    STRING_SESSION = environ.get("STRING_SESSION", "1BVtsOGoBu2qLbRUJOUdqsPA9MhEDNntzqgc8wbXV5o64_8DboVFFt8vDCHerEBG_cI0FPcpevCnHTl2HOhTyZPNoxbSeUxnnu0Pt-ebx4mplxfOEkE74QoACGjqTR_SReVMQ7Ozv3eUciyri-erhSISE9a4CB6wiT66oMwtQZsSW2YLT3LiFokFylf8pI0qeunOzK1qbRkof9BL43o-Qj0ykCMzql8MQXwp0aMt7-WhtvHPMz3VX9TYQ4jdrAsSI2sa6YukDpBShz4tSflhIVR78xJmwk_Ej6_BS_G4LFrHfiZr78WQilPzxKDyv9utCPAVWzLbpzwCnEAoJerMppMmOpPpUFd4=")
    SUDO_USERS = environ.get("SUDO_USERS", "1408595569 786843013")
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
