import time
import random

from instabot import Bot

bot = Bot()

bot.logout()

time.sleep(
    (60 * 5) + random.randint(0, 60 * 5) + random.random()
    # at least 5 minutes
)

bot.login(
    # if in threaded scheduled job
    is_threaded=True,
    # ----------------------------
    use_cookie=False,
    use_uuid=True
)