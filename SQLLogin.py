import tkinter as t
import pyodbc

class SQL_Server_Login:
    def __init__(self):
        self.main_window = t.Tk()


        self.main_window.geometry('300x100')
        self.main_window.title('SQL Server Login')

        self.username_frame = t.Frame(self.main_window)
        self.password_frame = t.Frame(self.main_window)
        self.button_frame = t.Frame(self.main_window)

        self.login_label = t.Label(self.username_frame, text='Login:')
        self.login_label.pack(side='left')

        self.login_entry = t.Entry(self.username_frame, width=20)
        self.login_entry.pack(side='left')

        self.password_label = t.Label(self.password_frame, text='Password:')
        self.password_label.pack(side='left')

        self.password_entry = t.Entry(self.password_frame, show='*', width=20)
        self.password_entry.pack(side='left')

        self.login_button = t.Button(self.button_frame, text='Login', command=self.access_database)
        self.login_button.pack()

        self.username_frame.pack(side='top')
        self.password_frame.pack(side='top')
        self.button_frame.pack(side='top')

        t.mainloop()

    def access_database(self):
        user_name = self.login_entry.get()
        password = self.password_entry.get()

        self.main_window.destroy()

        preList = {}
        courseList = []
        cn_str = (

    'Driver = {SQL Server Native Client 11.0};'
    'Server=MIS-SQLJB;'
    'Database=School;'
    'UID='+user_name+';'
    'PWD='+password+';'
    )

        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()
        cursor.execute('select * from School.dbo.Course')

myInstance = SQL_Server_Login()