import tkinter as t

class SQL_Server_Login:
    def __init__(self):
        self.main_window = t.Tk()


        self.main_window.geometry('400x200')
        self.main_window.title('SQL Server Login')

        self.username_frame = t.Frame(self.main_window)
        self.password_frame = t.Frame(self.main_window)
        self.button_frame = t.Frame(self.main_window)

        self.login_label = t.Label(self.username_frame, text='Login:')
        self.login_label.pack(side='left')

        self.login_entry = t.Entry(self.username_frame, width=10)
        self.login_entry.pack(side='left')

        self.password_label = t.Label(self.password_frame, text='Password:')
        self.password_label.pack(side='left')

        self.password_entry = t.Entry(self.password_frame, show='*', width=10)
        self.password_entry.pack(side='left')

        #self.login_button = t.Button(self.button_frame, text='Login', command=)
        self.username_frame.pack(side='top')
        self.password_frame.pack(side='top')
        self.login_label.pack(side='top')

        t.mainloop()
myInstance = SQL_Server_Login()