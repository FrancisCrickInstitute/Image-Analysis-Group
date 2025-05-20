To install CellPose to run properly on a jupyter notebook on the HPC cluster (nemo) you should follow the following steps:

** Be sure to use a GPU node while installing! **
•	Download the files "install_cellpose_0525.sh" and "Cellpose_GPU_Check.ipynb" to a folder on nemo (labname/working/username/cellpose0525 or something)
•	Open an ondemand desktop session on a gpu node
•	Open a terminal window on ondemand
•	Navigate on the command line to the place where the files were downloaded
•	Type in ./install_cellpose_0525.sh on the command line when you are in the folder where the files are downloaded
•	Wait a few minutes for everything to install (it won’t install super quick, so if it is quick, it’s not right)
•	When done, open up a jupyter session on ondemand on a gpu node
•	Open the notebook "Cellpose_GPU_Check.ipynb", which you’ve saved to cellpose folder on nemo
•	Run the two cells, if it works and comes up true, all installed

For a demonstration of running Cellpose-SAM on images, please see this notebook:


