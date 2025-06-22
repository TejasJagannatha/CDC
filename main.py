# - @ BPA Automation Scripts- For Personal Use
# -----
# Author
# Tejas Jagannatha
#Connect me on Linkedin: https://www.linkedin.com/in/tejas-jagannatha-450559147/
# ------
import time, pyperclip, os, datetime
from db import collection
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import threading


#directory= input(r'Set Working Directory where you want results to store:')
#os.chdir(directory)
directory= os.getcwd()
pyperclip.copy("")

app= FastAPI()
stop_event = threading.Event()
def copy():
    data = pyperclip.paste()
    return data


def write_toMongo(file_write):
    def wrapper(cp_data):
        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        file_write(cp_data)
        data_mongo= {'timestamp': timestamp, 'logged_data': cp_data}
        collection.insert_one(data_mongo)

    return wrapper


@write_toMongo
def write_todb(data):
    with open('critical_data_copied.txt', 'a') as file:
        file.write(data + '\n')



def run_task():
    stop_event.clear()
    last_copied_data = None  # Initialize variable to store the last copied data
    while not stop_event.is_set():
        if pyperclip.paste()!= "":
            data_copied = copy()
            if data_copied != last_copied_data:  # Check if newly copied data is different
                write_todb(data_copied)
                last_copied_data = data_copied  # Update last copied data

@app.get('/cdc')
def start_cdc():
    threading.Thread(target=run_task,daemon= True).start()
    return f"The machine has been started to capture"


@app.get('/stop')
def stop_cdc():
    stop_event.set()
    return f"The machine has stopped and the data has been saved to {directory}"


@app.get('/help', response_class=PlainTextResponse)
def help():
    contains= ["The project is innovated and developed by @Tejas Jagannatha", "Connect me on Linkedin: https://www.linkedin.com/in/tejas-jagannatha-450559147/",
               "Use curl command to hit the api /cdc to start the application which will trigger infinite copy.",
               "Use curl command to hit the api /stop to stop the application and it shows the place where all the final copied datas are stored for your use"
               ]
    return "\n".join(contains)