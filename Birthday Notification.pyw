from plyer import notification
import time
birthdayFile = 'D:/PythonProjects/Birthday_data.txt'

def checkTodayBirthday():
    file = open(birthdayFile, 'r')
    today = time.strftime('%d-%B')
    flag = 0
    print(today)
    for line in file:
        if today in line:
            print (today)
            line = line.split(' ')
            print(line)
            flag = 1
            notification.notify(title = "Birthday Reminder",
                            message = "Birthdays Today: {} {} ".format(line[1],line[2]),
                            timeout = 10)
    if flag == 0:
        notification.notify(title = "Birthday Reminder", message =" No Birthdays Today! ", timeout = 5)

checkTodayBirthday()

