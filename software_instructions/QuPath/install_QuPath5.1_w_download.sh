\#!/bin/bash

#get file from https://github.com/qupath/qupath/releases/download/v0.5.1/QuPath-v0.5.1-Linux.tar.xz
#written by Todd Fallesen.  Updated by Todd Fallesen Jan 23, 2026

current_directory=$(pwd)
QuPath_URL="https://github.com/qupath/qupath/releases/download/v0.5.1/QuPath-v0.5.1-Linux.tar.xz"
filename=$(basename "$QuPath_URL")

wget -O "$current_directory/$filename" "$QuPath_URL"

#unzip the file
tar -xf QuPath*

#remove the zip file
remove_if_exists() {
    local file="$1"

    if [[ -f "$file" ]]; then
        rm "$file"
        echo "Removed $file"
    else
        echo "File not found, skipping removal: $file"
    fi
}
remove_if_exists "$current_directory/QuPath-v0.5.1-Linux.tar.xz"


#change directory to the QuPath/bin
cd QuPath-v0.5.1-Linux/QuPath/bin


#modify the permissions on QuPath launcher
chmod u+x QuPath

current_directory=$(pwd)
 
# Create a file in the home directory to save the current directory
output_file="$HOME/Run_QuPath.sh"

echo "cd $HOME/" > "$output_file"
echo "./QuPath" >> "$output_file"

echo "File created at: $output_file"

cd $HOME
chmod u+x $output_file
