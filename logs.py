import datetime
import json

def convert_code_to_text(code):
    if code == -1:   return "start bot"
    elif code == -2: return "stop bot"
    elif code == 0:  return "text"
    elif code == 1:  return "command"
    elif code == 2:  return "document"
    elif code == 3:  return "pinned"
    else:            return "none"

def json_data_to_write(chatid=0, code=0, text=""):
    dt = datetime.datetime.now()
    time = str(dt.day) + "_" + str(dt.month) + "_" + \
        str(dt.year) + "-" + str(dt.hour) + "_" + str(dt.minute)

    return json.dumps({
        "chatid": chatid,
        "format": convert_code_to_text(code),
        "text": text,
        "time": time
    })

def save(chatid=0, text="", code=0):
    list_data_write = json_data_to_write(chatid, code, text)
    with open('logs.txt', 'a', encoding="utf-8") as file:
        file.write(list_data_write + "\n")
        file.close()

def start():
    save(chatid=0, text="", code=-1)

def finish():
    save(chatid=0, text="", code=-2)
