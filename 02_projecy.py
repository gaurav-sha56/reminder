#This is a reminder app this app will give you reminders for your things
#keep learning
# still woring on this not completed yet

import openpyxl
import time
from datetime import datetime
from plyer import notification



if __name__=="__main__":
    task={}
    times=[]

    path = r"C:\Users\Gaurav Sharma\Documents\Project2\reminders.xlsx"
    wb_obj = openpyxl.load_workbook(path)  #object to load workbook
    sheet_obj = wb_obj.active  #object to activae workbook data of the cell row=1 and col=1 
    row=sheet_obj.max_row
    col=sheet_obj.max_column


    for i in range(1,row+1):   # list of tasks 
        cell_obj = sheet_obj.cell(row = i, column = 1)
        cell_obj_time = sheet_obj.cell(row = i, column = 2)
        # cell_obj_time.value=datetime.strftime("%H:%M:%S")
        task[cell_obj.value]=cell_obj_time.value
    print(task)
         
    

    condition = True
    while condition:
        c=datetime.now()
        current_time = c.strftime('%H:%M:%S')
        for i in times:
            if current_time==i:

                notification.notify(
                    title = "Reminder",
                    message = "Work",
                    timeout = 2 #displaying time
                )

                time.sleep(5)
                times.remove(i)
        if times==[]:
            condition = False
