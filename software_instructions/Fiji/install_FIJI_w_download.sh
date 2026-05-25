#!/bin/bash

current_directory="$(pwd)"
FIJI_URL="https://downloads.imagej.net/fiji/archive/20250514-1117/fiji-linux64.zip"
filename="$(basename "$FIJI_URL")"

wget -O "$current_directory/$filename" "$FIJI_URL"

#unzip the file
unzip "$filename"

#remove the zip file
rm -r fiji-linux64.zip

#change directory to the Fiji
cd Fiji.app

#modify the permissions on Fiji launcher
chmod u+x ImageJ-linux64

current_directory="$(pwd)"

# Create a file in the home directory to save the current directory
output_file="$HOME/Run_Fiji.sh"

{
  echo "cd \"$current_directory\""
  echo "./ImageJ-linux64"
} > "$output_file"

echo "File created at: $output_file"

cd $HOME
chmod u+x $output_file
