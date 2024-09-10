from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "6e7e2f5cdddba536b8e603b3155223c1")
      API_ID = int(getenv("API_ID", "27972068"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7027917459:AAFutNOcNOfpSkGR3D5nLiW-TlrWH3em1Vs")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002182758472").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
