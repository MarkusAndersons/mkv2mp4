import Tkinter as tk
import tkFileDialog as filedialog
import tkMessageBox as messagebox
import os
import sys
from subprocess import call

# tk settings
root = tk.Tk()
root.withdraw()

# env variables
isWindows = 0
isPosix = 0

def checkDetails():
    # check OS
    if os.name == 'nt':
        isWindows = 1
    elif os.name == 'posix':
        isPosix = 1
    else:
        print("ERROR: Unsupported system")
        print("Your system is " + os.name)
        messagebox.showinfo("ERROR", "Sorry, " + os.name + " is unsupported at this time")
        sys.exit()
    # check if FFmpeg installed
    

def convert():
    x = 1

checkDetails()

# file selector
file_path = filedialog.askopenfilename()
