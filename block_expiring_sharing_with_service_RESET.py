import time
import datetime

# EXAMPLE OF RESPONSE
# the response will send a block expiring after 24h from now
# TODO: response json is incomplete
# --------------------------------------------------------------------------------------
block_time = 24 * 60 * 60
block_timestamp = time.localtime(time.time() + block_time)
block_date = time.strftime("%Y-%m-%d", block_timestamp)
json_reponse = {
    "message": "feedback_required",
    "spam": True,
    "feedback_title": "Action Blocked",
    "feedback_message": "Your account has been temporarily blocked from taking this action. Sharing your account with a service that helps you get more likes or followers goes against our Community Guidelines. This block will expire on {}. Tell us if you think we made a mistake.".format(
        block_date
    ),
    "feedback_url": "repute/report_problem/user_restriction_LIKE_RESTRICT/",
    "feedback_appeal_label": "Tell us",
    "feedback_ignore_label": "OK",
    "feedback_action": "report_problem",
    "status": "fail",
}
# --------------------------------------------------------------------------------------


# GENERAL PURPOSE RESET
# wait till declared expiry date
# --------------------------------------------------------------------------------------
expiry_date = json_reponse["feedback_message"].split("will expire on ")[1].split(".")[0]

expiry_timestamp = time.mktime(
    datetime.datetime.strptime(expiry_date, "%Y-%m-%d").timetuple()
)

expiry_sleep = expiry_timestamp - time.time()

print(
    "Expires: {} - timestamp: {} - wait: {} seconds".format(
        expiry_date, expiry_timestamp, expiry_sleep
    )
)

time.sleep(expiry_sleep)
# --------------------------------------------------------------------------------------
