# - @ BPA Automatiob Scripts- For Personal Use
# -----
# Author
# Tejas Jagannatha
#Connect me on Linkedin: https://www.linkedin.com/in/tejas-jagannatha-450559147/
# ------

import time, pyperclip, os, datetime
directory= input(r'Set Working Directory where you want results to store:')
os.chdir(directory)
print('*' * 10)
print('Thanks for Cloning me: ')

for i in range(0, 6):
    print('.')
    time.sleep(1.1)
    print('.')
print('======# #=========')

def copy():
    data = pyperclip.paste()
    return data
def write_todb(data):
    with open('critical_data_copied.txt', 'a') as file:
        file.write(data + '\n')

for i in range(0, 4):
    print('.')
current_time = datetime.datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Current Time you started:", timestamp)

last_copied_data = None  # Initialize variable to store the last copied data

while True:
    data_copied = copy()
    if data_copied != last_copied_data:  # Check if newly copied data is different
        write_todb(data_copied)
        last_copied_data = data_copied  # Update last copied data
    time.sleep(0.4)  # Pause









