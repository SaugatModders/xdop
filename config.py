from sample_config import Config
Noi

class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 22078178
    API_HASH = "d8b5fdd23f55a4ae9f709807b88406be"
    # the name to display in your alive message
    ALIVE_NAME = "Harpreet"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:harop11@localhost:5432/catuserbot"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBuwHhAWvxVy_N0-NyAX2TtwVd2FPSgJ-fN-BsoeuoEMIGf86CbSAPLo2e4bZYnOVCayQC-4FiZAFqH0fEHzOYTlqI1sppRRLVYyRJ341aiUiedWmwzwnD3bQ1Gf3FpLMfanxDu-nxwHOHezOgPuHafJK46h4Nb4oLwji6sVx1gwSF3Zlwd6Ir1YbThTGw4LI5n_U00FCScYTKPf99gLE3if3_LfextkIkLI38seU9aVPh-tPWDMWVW7Ze6sQ-4LHJcHttZRydgwJsERF0mgO9oLAP5kItI0ffz90wxnL6khmPCLy_a1sFxQlj9yD-CrdYdZ5NmkCP5puWyymj8U-kK2E="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5953662646:AAFLdwH_SUrt2vu_E0-i6B6khjVPmb9NSlw"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001847145903
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
