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
ffmpegLocation = None

# to find the ffmpeg exe
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def checkDetails():
    global isWindows
    global isPosix
    global ffmpegLocation
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
    ffmpegLocation = which("ffmpeg")
    if ffmpegLocation is None:
        ffmpegLocation = which("C:\\\\ffmpeg\\ffmpeg.exe")
        if ffmpegLocation is None:
            print("ERROR: ffmpeg not installed")
            messagebox.showinfo("ERROR", "The ffmpeg executable cannot be found, please make sure you have correctly installed this program and all dependencies")
            sys.exit()

def convert(filename):
    outName = filename[:-4] + ".mp4"
    print outName
    print filename
    result = call(ffmpegLocation + " -i \"" + filename + "\" -c copy \"" + outName + "\"", shell = True)
    if result != 0:
        messagebox.showinfo("ERROR", "An error occured with the call to ffmpeg, to troubleshoot, run this program again from the terminal")
        sys.exit()

checkDetails()

# file selector
file_path = filedialog.askopenfilename()
root.update()
if file_path is not None:
    convert(file_path)
