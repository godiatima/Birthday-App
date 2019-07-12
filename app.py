# Python program for birthday reminder application
# time module is must as reminder is set with the help of dates
import time
# os module is used to notify user
# using default "ubuntu notification"
import os

birthdayFile = 'reminder.data'

def checkTodaysBirthdays():
	fileName = open(birthdayFile, 'r')
	today = time.strftime('%m%d')
	flag = 0
	for line in fileName:
		if today in line:
			line = line.split(' ')
			flaf = 1
			# line [1] contains name and line [2] contains surname
			os.system('notify-send "Birthdays Today: ' + line[1] + ' ' + line[2] + '"')
	if flag == 0:
			os.system('notify-send "No Birthdays Today!"')

if __name__ == '__main__':
	checkTodaysBirthdays()









