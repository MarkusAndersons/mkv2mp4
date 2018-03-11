#!/bin/bash
# check if root
if [ "$EUID" -ne 0 ]
    then echo "Must be root"
    echo "Usage: sudo bash install.sh"
    exit 1
fi

if [ "$1" == "uninstall" ] ; then
    rm -rf /usr/local/mkv2mp4_files
    rm /usr/local/bin/mkv2mp4
    echo "Uninstalled"
    exit 0
fi
# check for python
command -v python >/dev/null 2>&1 || {
    echo "ERROR - Python must be installed"
    exit 2
}

#   check if already installed
command -v ffmpeg >/dev/null 2>&1 || {
    echo "Installing ..."
    echo "---------------------"
    echo "Downloading ..."
    curl -o ffmpeg.tar.bz2  'https://cdn.markusandersons.com/static/ffmpeg.tar.bz2'
    tar -xzvf ffmpeg.tar.bz2
    mv ffmpeg /usr/local/bin
    rm ffmpeg.tar.bz2
    echo "Installed ffmpeg"
}

mkdir /usr/local/mkv2mp4_files
cp mkv2mp4.py /usr/local/mkv2mp4_files
touch /usr/local/bin/mkv2mp4
echo "python ../mkv2mp4_files/mkv2mp4.py" >> /usr/local/bin/mkv2mp4
chmod +x /usr/local/bin/mkv2mp4
echo "Installed mkv2mp4"
