import json
import os
import sys
from slacksocket import SlackSocket


SLACK_API_KEY = os.environ["SLACK_API_KEY"]

s = SlackSocket(SLACK_API_KEY)


def mainloop():
    for event in s.events():

        obj = json.loads(event.json)

        if not obj["type"] == "message":
            continue

        user = obj["user"]
        message = obj["text"]
        channel = obj["channel"]

        if 'VEP' not in message.upper():
            continue

        reply_text = "@{} Pythonはいいぞ！".format(user)

        if __debug__:
            print(reply_text)
        else:
            try:
                s.send_msg(reply_text, channel_name=channel)
            except Exception as e:
                print(e, file=sys.stderr)


if __name__ == '__main__':
    mainloop()


