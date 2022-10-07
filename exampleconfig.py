from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
    # the name to display in your alive message
    ALIVE_NAME = "billi hu"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:harop@localhost:5432/catuserbot"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "Your value"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "1BJWap1wBu4BqeBipo1GshCV__CjOdajIJ3ZkLu7tbX9x6QOpg-gNpAsrOBG1khg3iCTCSmhQR3DyNKG2LmFOpdg21yRz3IpI1irZknw-q5bTcQ790bSQxrMPzmfNXD3nXecGRq2_uQOfB6ve-gg1JHhEuv2BLT-AE6NDX8iomXG87u12SO3MP8MEE3NPO5T7bZPF25owytibevkNUNtlMOrSs6kPqveGk1iUMbXCvpgwzzL-krzt_YPp0vyEO1Kl3He2joWD05Ss-lQBpZv7CVa07lDRDMFAaKQ7lT9KsQJ7rHWyd-DrE4n7R-nGZ7Ybv379dZP140Hk1N5HYSkvJzyrMVLxm-I="
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
