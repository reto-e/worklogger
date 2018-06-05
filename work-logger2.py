import gspread
from oauth2client.service_account import ServiceAccountCredentials
import RPi.GPIO as GPIO
import datetime
import time
import csv

scope = ['https://spreadsheets.google.com/feeds',
     	'https://www.googleapis.com/auth/drive']

#http://gspread.readthedocs.io/en/latest/oauth2.html
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

def writeLogEntry(btn):
	timeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	try:
		task = tasks[btn]
		entry = [timeStamp, task, "-"]
		with open("/home/pi/Dokumente/work-logger/workLog.csv", "a") as file:
			writer = csv.writer(file, quoting=csv.QUOTE_ALL)
			writer.writerow(entry)

        gc = gspread.authorize(credentials)
        wks = gc.open("gdrive-worklog").sheet1
        wks.append_row(entry)

	except:
		print("no task defined")

def readTasksFromFile():
	taskFile = open("/home/pi/Dokumente/work-logger/tasks.txt", "r")
	tasksRaw = taskFile.readlines()
	for task in tasksRaw:
		task = task.replace("\n","")
		tasks.append(task)
		print(task)

def switchOffAllLed():
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(9, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)

tasks = []
readTasksFromFile()

GPIO.setmode(GPIO.BCM) # set GPIO numbering

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setup(2, GPIO.OUT) #led btn1
GPIO.setup(3, GPIO.OUT) #led btn2
GPIO.setup(4, GPIO.OUT) #led btn3
GPIO.setup(17, GPIO.OUT) #led btn4
GPIO.setup(27, GPIO.OUT) #led btn5
GPIO.setup(22, GPIO.OUT) #led btn6
GPIO.setup(10, GPIO.OUT) #led btn7
GPIO.setup(9, GPIO.OUT) #led btn8
GPIO.setup(11, GPIO.OUT) #led btn9

# blink when ready
for x in range(0, 3):
        GPIO.output(2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(2, GPIO.LOW)
        time.sleep(0.5)

# start control loop
while True:
	btn1 = GPIO.input(18)
	btn2 = GPIO.input(23)
	btn3 = GPIO.input(24)
	btn4 = GPIO.input(25)
	btn5 = GPIO.input(8)
	btn6 = GPIO.input(7)
	btn7 = GPIO.input(1)
	btn8 = GPIO.input(12)
	btn9 = GPIO.input(16)

	if btn1 == False: # false means: button pressed
		writeLogEntry(0)
		switchOffAllLed()
		GPIO.output(2, GPIO.HIGH)
		time.sleep(0.2)

	if btn2 == False: # false means: button pressed
		writeLogEntry(1)
		switchOffAllLed()
		GPIO.output(3, GPIO.HIGH)
		time.sleep(0.2)

	if btn3 == False: # false means: button pressed
		writeLogEntry(2)
		switchOffAllLed()
		GPIO.output(4, GPIO.HIGH)
		time.sleep(0.2)

	if btn4 == False: # false means: button pressed
		writeLogEntry(3)
		switchOffAllLed()
		GPIO.output(17, GPIO.HIGH)
		time.sleep(0.2)

	if btn5 == False: # false means: button pressed
		writeLogEntry(4)
		switchOffAllLed()
		GPIO.output(27, GPIO.HIGH)
		time.sleep(0.2)

	if btn6 == False: # false means: button pressed
		writeLogEntry(5)
		switchOffAllLed()
		GPIO.output(22, GPIO.HIGH)
		time.sleep(0.2)

	if btn7 == False: # false means: button pressed
		writeLogEntry(6)
		switchOffAllLed()
		GPIO.output(10, GPIO.HIGH)
		time.sleep(0.2)

	if btn8 == False: # false means: button pressed
		writeLogEntry(7)
		switchOffAllLed()
		GPIO.output(9, GPIO.HIGH)
		time.sleep(0.2)

	if btn9 == False: # false means: button pressed
		writeLogEntry(8)
		switchOffAllLed()
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.2)
