# mkv2mp4
A simple GUI for converting .mkv files to .mp4 using the ffmpeg library. The program is written entirely in Python and is compatible cross-platform (tested on macOS Sierra and Windows 10).

## Installation
To install on macOS or another Unix system, run
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
As it is installed in */usr/local/bin*, it should be in your path, so simply running
```bash
$ mkv2mp4
```
in the command line should be all that is needed for it to start.
