import datetime
import json

def convert_format_message_idage(message_id):
    if message_id == -2:
        return "stop bot"
    elif message_id == -1:
        return "start bot"
    elif message_id == 0:
        return "message_idage"
    elif message_id == 1:
        return "command"
    elif message_id == 2:
        return "document"
    elif message_id == 3:
        return "pinned"
    else:
        return "none"

def save(chatid=0, text="", formattext=0):

    dt = datetime.datetime.now()
    settime = str(dt.day) + "_" + str(dt.month) + "_" + \
            str(dt.year) + "-" + str(dt.hour) + "_" + str(dt.minute)

    list = json.dumps({
        "chatid": chatid,
        "format": convert_format_message_idage(formattext),
        "text": text,
        "datetime": settime
    })

    with open('logs/logs.txt', 'a', encoding="utf-8") as f:
        f.write(list + "\n")
        f.close()
