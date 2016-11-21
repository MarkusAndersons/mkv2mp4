# mkv2mp4
A simple GUI for converting .mkv files to .mp4 using the ffmpeg library. The program is written entirely in Python and is compatible cross-platform (tested on macOS Sierra and Windows 10).

## Installation
If you only want to use the application, simply download the "*release*" folder.

To install on Windows, simply double-click on the "install" executable in the release/windows folder. This will install Python 2.7 and FFmpeg into the root of your directory. Another batch file will be copied onto the desktop.

To install on macOS or another Unix system, change directory to *./unix/* in the terminal. Then run
```bash
$ sudo bash install.sh
```
This will install the ffmpeg executable (if it doesn't already exist) and the *mkv2mp4* executable. This will be placed in */usr/local/bin*.

On Unix systems, it can also be uninstalled by running
```bash
$ sudo bash install.sh uninstall
```
NOTE: The Unix install script will not install Python, if it is not installed on the system, please install it through the usual methods.

## Usage
To use the application on Windows, simply double-click on the batch script on the desktop and select the MKV file you wish to convert from the dialog displayed.
