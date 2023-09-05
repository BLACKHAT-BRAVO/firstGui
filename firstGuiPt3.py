from tkinter import *
import firebase_admin
from firebase_admin import db, credentials
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
from datetime import datetime
  
cred = credentials.Certificate("credentials.json")

firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://firgui-default-rtdb.firebaseio.com/'
    })


ref = db.reference('py/')

root = Tk()



#Function called to check if the ID entered is in the database and sends user to appropriate screen
def check_user_id():
    global entry, third_window
    user_id = entry.get()
    user_ref = ref.child('users').child(user_id)
    user_data = user_ref.get()
    
    print("User Data:", user_data)  # Add this line
    
    if user_data is None:
        messagebox.showwarning("Error", "Invalid user ID")
    else:
        user_status = user_data.get("Status")
        user_type = user_data.get("Type")
        print("User Status:", user_status)
        print("User Type:", user_type)
        
        if user_status == "Suspended":
            messagebox.showerror("Error", "Your account is suspended")
        else:
            third_window.destroy()
            if user_type == "Admin":
                adminHub(user_id)
            elif user_type in ["Staff", "Faculty", "Janitor", "Student"]:
                swipeMenu(user_id)
            else:
                messagebox.showerror("Error", "Invalid user type")

#Home Screen/Input ID screen
def inputID():
 global entry, third_window

 third_window = Toplevel(root)
 third_window.title("SUN Lab Access System")
    
 def close_third_window():
        third_window.destroy()
        root.deiconify()  # Show the main window again
    
    
 third_window.protocol("WM_DELETE_WINDOW", close_third_window)
    
 frame_swipe = Frame(third_window, padx=50, pady=30)
 frame_swipe.pack(expand=True, fill="both")

 label0 = Label(frame_swipe, text="Welcome to the SUN Lab Access System", font='Helvetica 18 bold')
 label0.pack(side="top", anchor="center", pady=75)
    
 label1 = Label(frame_swipe, text="Please Enter Your ID 🙂", font='Helvetica 18')
 label1.pack(side="top", anchor="center", pady=5)
    
 entry = Entry(frame_swipe, width = 35, borderwidth=5)
 entry.pack(side="top", anchor="center", pady=20)

 button_submit = Button(frame_swipe, text="Submit", padx=40, pady=10, fg= "blue", command=check_user_id)
 button_submit.pack(side="top", anchor="center", pady=20)

 button_back = Button(frame_swipe, text="Exit Program", padx=23, pady=11, fg= "red", command=root.quit)
 button_back.pack(side="bottom", anchor="center", pady=10)
 
 root.withdraw()


#Swipe screen for all users except for Admin
def swipeMenu(userID):
    second_window = Toplevel(root)
    second_window.title("Swipe Register")
    
    def close_second_window():
        second_window.destroy()
        inputID() # Show the main window again
    
    second_window.protocol("WM_DELETE_WINDOW", close_second_window)
    
    frame_swipe = Frame(second_window, padx=50, pady=30)
    frame_swipe.pack(expand=True, fill="both")
    
    label1 = Label(frame_swipe, text="Welcome to the Swipe Register 🏂", font='Helvetica 18 bold')
    label1.pack(side="top", anchor="center", pady=30)
    
    swipe_in_button = Button(frame_swipe, text="Swipe In ✅", padx=44, pady=30, fg= "green", bg="black", command=lambda: ActivateSwipeIn(userID))
    swipe_in_button.pack(side="top", anchor="center", pady=20)
    
    swipe_out_button = Button(frame_swipe, text="Swipe Out ❌", padx=40, pady=30,fg= "red", bg="black", command=lambda: ActivateSwipeOut(userID))
    swipe_out_button.pack(side="top", anchor="center", pady=20)
    

    button_back = Button(frame_swipe, text="Go Home 🏠", padx=40, pady=10, command=close_second_window)
    button_back.pack(side="bottom", anchor="center", pady=10)

    root.withdraw()

#Admin Screen
def adminHub(userID):
    global admin_window
    admin_window = Toplevel(root)
    admin_window.title("Administrator Control Center")
    
    def close_admin_window():
        admin_window.destroy()
        inputID()  # Show the main window again
    
    admin_window.protocol("WM_DELETE_WINDOW", close_admin_window)
    
    frame_swipe = Frame(admin_window, padx=50, pady=30)
    frame_swipe.pack(expand=True, fill="both")
    
    label1 = Label(frame_swipe, text="🚨 Welcome to the Administrator's Control Room 🚨", font='Helvetica 18 bold')
    label1.pack(side="top", anchor="center", pady=30)
    
    browseSwipe = Button(frame_swipe, text="Browse Swipe History 💳", padx=53, pady=30, fg="brown", command=browseHistory)
    browseSwipe.pack(side="top", anchor="center", pady=20)
    
    browseUsers = Button(frame_swipe, text="Browse Authorized Users 🔐", padx=44, pady=30, fg="blue", command= browseID)
    browseUsers.pack(side="top", anchor="center", pady=20)

    aOsUsers = Button(frame_swipe, text= "Activate or Suspend Users 🤪", padx=40, pady=30, fg="purple", command= lambda : AoSentry(userID))
    aOsUsers.pack(side="top", anchor="center", pady=20)

    #Swipe IN or OUT
    swipe_in_button = Button(frame_swipe, text="Swipe In ✅", padx=95, pady=30, fg= "green", bg="black", command=lambda: ActivateSwipeIn(userID))
    swipe_in_button.pack(side="top", anchor="center", pady=20)
    
    swipe_out_button = Button(frame_swipe, text="Swipe Out ❌", padx=91, pady=30,fg= "red", bg="black", command=lambda: ActivateSwipeOut(userID))
    swipe_out_button.pack(side="top", anchor="center", pady=20)

    #Go to ID input
    button_back = Button(frame_swipe, text="Go Home 🏠", padx=50, pady=10, command=close_admin_window)
    button_back.pack(side="bottom", anchor="center", pady=10)

    root.withdraw()

#Activate or suspend function
def AoSentry(userID):
    global entry, fourth_window, admin_window

    admin_window.destroy()
    
    fourth_window = Toplevel(root)
    fourth_window.title("SUN Lab Access System")
    
    def close_fourth_window():
        fourth_window.destroy()
        adminHub(userID)
        #root.deiconify()  # Show the main window again
    
    
    fourth_window.protocol("WM_DELETE_WINDOW", close_fourth_window)
    
    frame_swipe = Frame(fourth_window, padx=50, pady=30)
    frame_swipe.pack(expand=True, fill="both")

    label0 = Label(frame_swipe, text="Welcome to the Master Entry User System", font='Helvetica 18 bold')
    label0.pack(side="top", anchor="center", pady=75)
    
    label1 = Label(frame_swipe, text="Please Enter the User ID 😈", font='Helvetica 18')
    label1.pack(side="top", anchor="center", pady=5)
    
    entry = Entry(frame_swipe, width = 35, borderwidth=5)
    entry.pack(side="top", anchor="center", pady=20)

    button_submit = Button(frame_swipe, text="Submit", padx=40, pady=10, command=checkVictim)
    button_submit.pack(side="top", anchor="center", pady=20)

    button_back = Button(frame_swipe, text="Go Back", padx=23, pady=11, command= close_fourth_window)
    button_back.pack(side="bottom", anchor="center", pady=10)
 
    root.withdraw()  

def checkVictim():
    global entry, fourth_window
    user_id = entry.get()
    user_ref = ref.child('users').child(user_id)
    user_data = user_ref.get()
    
    print("User Data:", user_data)  # Add this line
    
    if user_data is None:
        messagebox.showwarning("Error", "Invalid user ID")
    else:
        user_type = user_data.get("Type")
        print("User Type:", user_type)  # Add this line
        fourth_window.destroy()  # Close the ID Register window
        if user_type == "Admin":
            messagebox.showerror("Error", "Invalid user type")
        elif user_type in ["Staff", "Faculty", "Janitor", "Student"]:
            ControlMenu(user_id)
        else:
            messagebox.showerror("Error", "Invalid user type")
            messagebox.showerror("Error", "Invalid user type")

def ControlMenu(user_id):
    second_window = Toplevel(root)
    second_window.title("Activation and Suspension Panel")
    
    def close_second_window():
        second_window.destroy()
        inputID() # Show the main window again
    
    second_window.protocol("WM_DELETE_WINDOW", close_second_window)
    
    frame_swipe = Frame(second_window, padx=50, pady=30)
    frame_swipe.pack(expand=True, fill="both")
    
    label1 = Label(frame_swipe, text="Welcome to the Activation/Suspension Program 👽", font='Helvetica 18 bold')
    label1.pack(side="top", anchor="center", pady=30)
    
    activate_button = Button(frame_swipe, text="Activate User", padx=44, pady=30, fg= "green", bg="black", command=lambda: ActivateMessage(user_id))
    activate_button.pack(side="top", anchor="center", pady=20)
    
    suspend_button = Button(frame_swipe, text="Suspend User", padx=42, pady=30,fg= "red", bg="black", command=lambda: SuspendMessage(user_id))
    suspend_button.pack(side="top", anchor="center", pady=20)
    

    button_back = Button(frame_swipe, text="Go Home", padx=40, pady=10, command=close_second_window)
    button_back.pack(side="bottom", anchor="center", pady=10)

    root.withdraw()

def browseHistory():
    access_ref = ref.child('access')
    access_data = access_ref.get()
    
    if not access_data:
        messagebox.showinfo("Info", "No swipe records found!")
        return

    # Sort the data by timestamp
    sorted_access_data = sorted(access_data.items(), key=lambda x: x[1]["Time Stamp"], reverse=True)

    # Create a new window for displaying the history
    history_window = Toplevel(root)
    history_window.title("Swipe Records")
    
    admin_window.withdraw()
    
    def close_history_window():
        history_window.destroy()
        admin_window.deiconify()

    frame_history = Frame(history_window, padx=75, pady=50)
    frame_history.pack(expand=True, fill="both")
    
    tree = ttk.Treeview(frame_history, columns=("ID", "Name", "Timestamp", "Status"))
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Timestamp")
    tree.heading("#4", text="Status")
    
    for user_id, swipe_info in sorted_access_data:
        tree.insert("", "end", values=(user_id, swipe_info["Name"], swipe_info["Time Stamp"], swipe_info["In or Out"]))
        
    tree.pack(fill="both", expand=True)

    button_back = Button(frame_history, text="Go Back", padx=23, pady=11, command=close_history_window)
    button_back.pack(side="bottom", anchor="center", pady=10)

def browseID():
   users_ref = ref.child('users')
   users_data = users_ref.get()
    
   if not users_data:
        messagebox.showinfo("Info", "No authorized users found!")
        return

   # Create a new window to display the users
   browse_window = Toplevel(root)
   browse_window.title("Browse Authorized Users")

   # Hide the admin window while browseID window is active
   admin_window.withdraw()
    
   def close_browse_window():
        browse_window.destroy()
        admin_window.deiconify()

   frame_swipe = Frame(browse_window, padx=75, pady=30)  
   frame_swipe.pack(expand=True, fill="both")
    
   browse_window.protocol("WM_DELETE_WINDOW", close_browse_window)

   tree = ttk.Treeview(frame_swipe, columns=("ID", "Name"))  
   tree.heading("#1", text="ID")
   tree.heading("#2", text="Name")
    
   for user_id, user_info in users_data.items():
        tree.insert("", "end", values=(user_id, user_info["Name"]))

   tree.pack(fill="both", expand=True)

   button_back = Button(frame_swipe, text="Go Back", padx=23, pady=11, command= close_browse_window)
   button_back.pack(side="bottom", anchor="center", pady=10)


#Activates and Updates the Timestamp and Swipe in the database
def ActivateSwipeIn(userID):
     access_ref = ref.child('access').child(userID)
     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     access_ref.update({
        'In or Out': 'In',
        'Time Stamp': current_time  # Replace with the current timestamp
    })
     messagebox.showwarning("NOTICE", "You are SWIPED-IN")
   
#Updates the Timestamp and Swipe Out in the database
def ActivateSwipeOut(userID):
    access_ref = ref.child('access').child(userID)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    access_ref.update({
        'In or Out': 'Out',
        'Time Stamp': current_time  # Replace with the current timestamp
    })
    messagebox.showwarning("NOTICE", "You are SWIPED-OUT")
    

def ActivateMessage(userID):
    access_ref = ref.child('users').child(userID)
    access_ref.update({
        'Status': 'Activated',
    })
    messagebox.showwarning("NOTICE", "Account has been ACTIVATED")

def SuspendMessage(userID):
    access_ref = ref.child('users').child(userID)
    access_ref.update({
        'Status': 'Suspended',
    })
    messagebox.showerror("NOTICE", "Account has been SUSPENDED")

def ReactivateMessage():
    messagebox.showwarning("NOTICE", "Account has been REACTIVATED")


inputID()
root.mainloop()
