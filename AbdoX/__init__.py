from AbdoX.core.bot import Zelzaly
from AbdoX.core.dir import dirr
from AbdoX.core.git import git
from AbdoX.core.userbot import Userbot
from AbdoX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zelzaly()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
