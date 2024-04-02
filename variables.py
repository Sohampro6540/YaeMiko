# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 23040489  # Get this value from my.telegram.org/apps
    API_HASH = "4235beeabd4e5216fe412a00e444bb25"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ierjlkr:OG4dxzO67Zret3Zii43Hhvujkg89WVry0n9KsHE@karma.db.elephantsql.com/ierjlkr"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002036001760
    MESSAGE_DUMP = -1002036001760

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://t45:t45@cluster0.plfylpo.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "-1002036001760"
    SUPPORT_ID = -1002036001760

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7181246957:AAFjy_RYBxGfVcCzWh7qXnoQ85V7RMKBsIQ"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6574373060
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = [6574373060]  # Sudo users
    DEV_USERS = [6574373060]  # Dev users
    DEMONS = [6574373060]  # Support users
    TIGERS = 6574373060 # Tiger users
    WOLVES = [6574373060]  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
