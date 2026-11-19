#!/bin/bash

##Code written by Todd Fallesen, CALM @Crick.  todd.fallesen@crick.ac.uk.  If you have any questions, please hit us up. 

current_directory="$(pwd)"
filepath="/flask/apps/stardist/StarDist_Course_Materials/FIJI_Dec_2025/fiji_linux.zip"
filename="fiji_linux.zip"

cp $filepath $current_directory

#unzip the file
unzip $filename

#remove the zip file
rm -r $filename

#change directory to the Fiji
cd fiji_linux


#modify the permissions on Fiji launcher
chmod u+x ImageJ-linux64

current_directory="$(pwd)"

# Create a file in the home directory to save the current directory
output_file="$HOME/Run_Fiji_Trackmate.sh"

{
  echo "cd \"$current_directory\""
  echo "./ImageJ-linux64"
} > "$output_file"

echo "File created at: $output_file"

cd $HOME
chmod u+x $output_file
