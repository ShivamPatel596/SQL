import tkinter as t
import pyodbc

 

class ServerLogin:

    def __init__(self):

        self.main_window = t.Tk()
        self.main_window.geometry('300x100')
        self.main_window.title('SQL Server Login')

        self.frame1 = t.Frame(self.main_window)
        self.frame2 = t.Frame(self.main_window)
        self.frame3 = t.Frame(self.main_window)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        self.login_label = t.Label(self.frame1,text='Login:')
        self.login_label.pack(side='left',anchor='w')
        self.login_entry = t.Entry(self.frame1,width=15)
        self.login_entry.pack(side='right',anchor='e')

        self.pass_label = t.Label(self.frame2, text='Password:')
        self.pass_label.pack(side='left',anchor='w')
        self.pass_entry = t.Entry(self.frame2, show='*', width=15)
        self.pass_entry.pack(side='right',anchor='e')

        self.login_button = t.Button(self.frame3, text='Login', command=self.access_database)
        self.login_button.pack()

        t.mainloop()

    def access_database(self):
        login = self.login_entry.get()
        pw = self.pass_entry.get()
        self.main_window.destroy()

        #Password
        #MIS4322student

        preList = {}
        courseList = []
        cn_str = (

    'Driver={SQL Server};'
    'Server=MIS-SQLJB;'         #Server name
    'Database=School;'          #database name
    'UID='+login+';'            #user name
    'PWD='+pw+';'               #user password
    )

        cn = pyodbc.connect(cn_str)
        cursor = cn.cursor()
        cursor.execute('select name, budget from School.dbo.department')
        data = cursor.fetchall()
        dataList = []
        line = 'Dept Name				Original Budget		New Budget     Increase in Budget'
        dataList.append(line)
        for row in data:
            deptName = row[0]
            deptBudget = float(row[1])

            if deptName == 'Information Systems':
                newBudget = deptBudget * 1.2
            elif deptName == 'Computer Science':
                newBudget = deptBudget * 1.15
            else:
                newBudget = deptBudget * 1.1
            budgetIncrease = newBudget - deptBudget 
            line = (f'{deptName} ${deptBudget:<10,.2f} ${newBudget:,.2f} ${budgetIncrease:,.2f}')   
            dataList.append(line)
        for row in dataList:
            print(row)
            
'''     
        for row in data:
            courseID = row[0]
            title = row[1]
            credit = row[2]
            deptID = row[3]

            # courseList = [title, credit, deptID]
            # preList[courseID] = courseList

            preList = {'CourseID':courseID, 'Title':title, 'Credit':credit, 'DeptID':deptID}

            courseList.append(preList)
            print(preList)

 

        a = int(input("CourseID to search: "))

        for dictionary in courseList:
            if dictionary['CourseID'] == a:
                print(f'Title of the course: {dictionary["Title"]}')
                print(f'Credits for this course: {dictionary["Credit"]}')
                print(f'Dept ID for this course: {dictionary["DeptID"]}')
'''

myinstance = ServerLogin()