import time
import random

from instabot import Bot

bot = Bot()

# RESET working for like blocks
# it is still unclear if this works for follow blocks too
# ---------------------------------------------------------
bot.logout()

time.sleep(
    (60 * 5)
    + random.randint(0, 60 * 5)
    + random.random()
    # at least 5 minutes
)

bot.login(
    # if in threaded scheduled job only:
    # ----------------
    is_threaded=True,
    # ----------------
    use_cookie=False,
    use_uuid=True,
)
# ---------------------------------------------------------
