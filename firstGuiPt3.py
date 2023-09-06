from tkinter import *
import firebase_admin
from firebase_admin import db, credentials
from tkinter import messagebox



  
cred = credentials.Certificate("credentials.json")

firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://firgui-default-rtdb.firebaseio.com/'
    })


ref = db.reference('py/')

access_ref = ref.child('access')
access_ref.set({
        '1': {
        'Name': 'Thomson Toms',
        'ID': '0000',  
        'Time Stamp': 'Does not exist',
        'In or Out': 'Out'
    },
        '2' : {
        'Name': 'Hien Nyugen',
        'ID': '0001',
        'Time Stamp': 'Does not exist',
        'In or Out': 'Does not exist'
    },
        '3' : {
        'Name': 'Jeremy Blum',
        'ID': '0002',
        'Time Stamp': 'Does not exist',
        'In or Out': 'Does not exist'
    },
        '4' : {
        'Name': 'President Supreme Ruler',
        'ID': '0003',
        'Time Stamp': 'Does Not Exist',
        'In or Out': 'Does Not Exist'
        }                  })

users_ref = ref.child('users')
users_ref.set({
        '1': {
        'Name': 'Thomson Toms',
        'ID': '0000',
        'Type': 'Student',
        'Status': 'Activated'
    },
        '2' : {
        'Name': 'Hien Nyugen',
        'ID': '0001',
        'Type': 'Staff',
        'Status': 'Activated'
    },
        '3' : {
        'Name': 'Jeremy Blum',
        'ID': '0002',
        'Type': 'Faculty',
        'Status': 'Activated'
    },
        '4' : {
        'Name': 'President Supreme Ruler',
        'ID': '0003',
        'Type': 'Janitor',
        'Status': 'Activated'
        }           })






root = Tk()
root.title("SUN Lab Access System")



#frame where i have all buttons and labels from start screen in
frame = LabelFrame(root, padx=250, pady=100)
frame.pack()



#functions for all buttons
def swipeMenu():
    second_window = Toplevel(root)
    second_window.title("Swipe Register")
    
    def close_second_window():
        second_window.destroy()
        root.deiconify()  # Show the main window again
    
    second_window.protocol("WM_DELETE_WINDOW", close_second_window)
    
    frame_swipe = Frame(second_window, padx=50, pady=30)
    frame_swipe.pack(expand=True, fill="both")
    
    label1 = Label(frame_swipe, text="Welcome to the Swipe Register 🏂", font='Helvetica 18 bold')
    label1.pack(side="top", anchor="center", pady=30)
    
    swipe_in_button = Button(frame_swipe, text="Swipe In", padx=44, pady=30, fg= "green", bg="black", command=ActivateSwipeIn)
    swipe_in_button.pack(side="top", anchor="center", pady=20)
    
    
    swipe_out_button = Button(frame_swipe, text="Swipe Out", padx=40, pady=30,fg= "red", bg="black", command=ActivateSwipeOut)
    swipe_out_button.pack(side="top", anchor="center", pady=20)
    

    button_back = Button(frame_swipe, text="Back to Main Window", padx=40, pady=10, command=close_second_window)
    button_back.pack(side="bottom", anchor="center", pady=10)

    root.withdraw()

def adminHub():
    second_window = Toplevel(root)
    second_window.title("Administrator Control Center")
    
    def close_second_window():
        second_window.destroy()
        root.deiconify()  # Show the main window again
    
    second_window.protocol("WM_DELETE_WINDOW", close_second_window)
    
    frame_swipe = Frame(second_window, padx=50, pady=30)
    frame_swipe.pack(expand=True, fill="both")
    
    label1 = Label(frame_swipe, text="Welcome to the Administrator's Control Room 🤓", font='Helvetica 18 bold')
    label1.pack(side="top", anchor="center", pady=30)
    
    browseSwipe = Button(frame_swipe, text="Browse Swipe History", padx=53, pady=30, bg="#00FF00", command=ActivateSwipeIn)
    browseSwipe.pack(side="top", anchor="center", pady=20)
    
    browseUsers = Button(frame_swipe, text="Browse Authorized Users", padx=44, pady=30, bg="red", command=ActivateSwipeOut)
    browseUsers.pack(side="top", anchor="center", pady=20)

    aOsUsers = Button(frame_swipe, text= "Activate or Suspend Users", padx=40, pady=30, bg="red", command=ActivateSwipeOut)
    aOsUsers.pack(side="top", anchor="center", pady=20)

    button_back = Button(frame_swipe, text="Back to Main Window", padx=40, pady=10, command=close_second_window)
    button_back.pack(side="bottom", anchor="center", pady=10)

    root.withdraw()

def ActivateSwipeIn(userID):
    messagebox.showwarning("NOTICE", "You are SWIPED-IN")
   

def ActivateSwipeOut(userID):
    messagebox.showwarning("NOTICE", "You are SWIPED-OUT")
    

def ActivateMessage():
    messagebox.showwarning("NOTICE", "Account has been ACTIVATED")

def SuspendMessage():
    messagebox.showerror("NOTICE", "Account has been SUSPENDED")

def ReactivateMessage():
    messagebox.showwarning("NOTICE", "Account has been REACTIVATED")

#creating all  my labels and buttons
label1 = Label(frame, text="WELCOME HOME", font='Helvetica 18 bold')
label2 = Label(frame, text = "Choose your Identity")
myButton1 = Button(frame, text = "Administrator", padx = 34, pady= 10, command = adminHub, fg ="red")
myButton3 = Button(frame, text = "Faculty", padx = 53, pady= 10, command = swipeMenu, fg = "purple")
myButton5 = Button(frame, text = "Janitor", padx = 55, pady= 10, command = swipeMenu, fg = "#8B4000")
myButton2 = Button(frame, text = "Student", padx = 52, pady= 10, command = swipeMenu, fg = "green")
myButton4 = Button(frame, text = "Staff", padx = 61, pady= 10, command = swipeMenu, fg = "blue")
button_quit = Button(frame, text = "Exit Program", padx = 40, pady= 10, command = root.quit)



#For spacing
spaceLabel1 = Label(frame, text ="                         ")
spaceLabel2 = Label(frame, text ="                         ")
spaceLabel3 = Label(frame, text ="                         ")

#all layouts of labels and buttons in grid
label1.grid(row = 0, column = 0)
spaceLabel1.grid(row = 1, column = 0)
label2.grid(row = 2, column = 0)
spaceLabel2.grid(row = 3, column = 0)
myButton1.grid(row = 4, column = 0)
myButton2.grid(row = 5, column = 0)
myButton3.grid(row = 6, column = 0)
myButton4.grid(row = 7, column = 0)
myButton5.grid(row = 8, column = 0)
spaceLabel3.grid(row = 9, column = 0)
button_quit.grid(row = 10, column = 0)



root.mainloop()
