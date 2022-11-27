from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10584166
    API_HASH = "c6f089f20073c49ab67413655eecefa3"
    # the name to display in your alive message
    ALIVE_NAME = "billi hu"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:harop11@localhost:5432/catuserbot"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzgBu2L1qN381LHVqLv8zQXyhrZG-lkdUmZR5xhGaQstGhzHt8IpzRPstcTZo9SJH7rVh3Hb7f92UK87K3PkgM-hUTpdFrf_Xiuxee5pGqJgABCv8abnObJDsRGvGDKki5yRZlHFAWr9Yi6d2r_BQV5KtDsXcT8-ea7f-C72pebS4j46ePtS4v-65erJfkv4MKPk7GEWLk55i6r6xBgZiMsr_iEhr4y-KwFDxH9s8NvV5ctg1Ea1FUtH8ok6o3mK2XUbPvQJFHSFLFUyl6LRx14T5fBmW6DwO74f2kf6Fz-TT1pc0ZvQmeFIcyIuPMX78CyyLuqiFqhIrIUqSkZ0NiG6owQ="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5983929500:AAFulhGH3hzUybKyaKVUbe-JDIYoYW0aCTY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001805278464
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
