#!/bin/bash
# check if root
if [ "$EUID" -ne 0 ]
    then echo "Must be root"
    echo "Usage: sudo bash install.sh"
    exit 1
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
}

chmod +x convert_mkv
echo "Installed"
