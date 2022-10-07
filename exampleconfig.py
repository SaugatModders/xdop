from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10584166
    API_HASH = "c6f089f20073c49ab67413655eecefa3"
    # the name to display in your alive message
    ALIVE_NAME = "billi hu"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:harop@localhost:5432/catuserbot"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMgBuyKlmGUQqXD9ws1iCEd3YuiN7jyfI4HnXLGEQ2OXTv88wcNGvVTneb3pc3prWKaNpki2c8svpJG_CQwcM5TqdSY1yQp8Z6wCxb9PIDRikXcntGyrEqZ7HogHzfiDERydwWKNbTGBj2XbCLPaZZEEQio9S96MSGM-WFKkCPqpRUF545_pnQCPdTPpQH2guGAybakEe1ODlj1lietLt5cGSuxNOUqsTaecjzm96zbGQqGHvU_n4SXHmeuS6Ire_MulVRBcu9cPxNkThnF3W8fhBd5pg_NzLfvTnpBk57amL2bkXjMF01cRtIcvcjk65sjtnh7TrOvLWmiShUb8Vxf7z6w="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = ""
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001891414204
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
