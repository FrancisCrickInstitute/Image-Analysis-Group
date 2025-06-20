# How to install Cellpose on OnDemand

[Cellpose](https://github.com/MouseLand/cellpose) is a general model for cell and nuclear segmentation. The following is a simple, step-by-step guide to installing Cellpose on [OnDemand](https://openondemand.org/).

> More detailed information on installing Cellpose can be found [here](https://github.com/MouseLand/cellpose?tab=readme-ov-file#installation) if needed.

> ⚠️ **BEWARE** – the FIJI wrapper only works for cellpose version 3.0 (and below). If you have a newer version, you will have to create a new cellpose environment for FIJI to access an older version of it (see instructions below).


## Step 1: Open xterm
When your GPU OnDemand Desktop session starts, right click and select `xterm` to open a terminal:

![image](https://github.com/FrancisCrickInstitute/CALM/assets/31737822/c541950a-7dab-4641-982e-b657eb4e530c)

## Step 2: Load Anaconda
You need to set up a [conda](https://en.wikipedia.org/wiki/Conda_(package_manager)) environment, which will contain your Cellpose installation. To do this, you first need to load [Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)). Type the following in your terminal window and press `Enter`:
```shell
ml Anaconda3
```

## Step 3: Create Cellpose environment
You then need to create the environment that will contain the Cellpose installation, using the following command:
```shell
conda create --name cellpose-fiji python=3.11
```
In this example, the environment has been named `cellpose-fiji`, but you can call it whatever you want. The terminal will produce output similar to the following, where `user_name` will be replaced with whatever your user name is:
```shell
Retrieving notices: ...working... done
Collecting package metadata (current_repodata.json): done
Solving environment: done
 
## Package Plan ##
 
environment location: /camp/home/user_name/.conda/envs/cellpose-env

Proceed ([y]/n)?
```
Press `y` and `Enter` to proceed.

## Step 4: Activate environment
Activate your new Cellpose environment with the following command:
```shell
conda activate cellpose-fiji
```

## Step 5: Install Cellpose
At this point, it is important to note that you have merely created what is essentially an empty environment called `cellpose-fiji`. To actually install Cellpose within this environment, run the following series of commands:
```shell
pip install cellpose==3.0
```
The terminal will produce a large amount of output as the necessary packages are installed.     Press `y` and `Enter` to proceed.

## Step 6: Verify installation
To test whether the installation was successful, run the following:
```shell
cellpose --help
```
If the installation was successful, this should produce a list of all the parameters that can be used when running Cellpose.

## Step 7: Deactivate environment
You can now deactivate your Cellpose environment by running the following:
```shell
conda deactivate
```
## Step 8 (Optional): Run Cellpose as a GUI
To run the cellpose GUI you need to load VirtualGL before activating the conda environment for Cellpose. To load VirtualGL enter the following commands in the command line:
```shell
ml VirtualGL
conda activate cellpose-fiji
cellpose
```
Each step will take a few seconds

## Step 9 (Optional): Run Cellpose from FIJI
It is possible to run Cellpose directly from FIJI. Instructions for installing the necessary FIJI Plugin can be found [here](https://github.com/BIOP/ijl-utilities-wrappers?tab=readme-ov-file#ib-fiji---cellpose-wrapper).
To run from FIJI on OnDemand, you have to activate the environment before launching FIJI.
For example:
```shell
conda activate cellpose-fiji
```
When the conda environment is activated, it's name will show up in parentheses in the command line, so, launching FIJI will look like this:
```shell
(cellpose-fiji) ./ImageJ-linux64
```

## Step 10: Cite!
If you use Cellpose in your work, be sure to cite the relevant paper:
* Version 3 (Latest): Carsen Stringer and Marius Pachitariu. Cellpose3: one-click image restoration for improved cellular segmentation. _bioRxiv_ 2024.02.10.579780
* Version 2: Marius Pachitariu and Carsen Stringer. Cellpose 2.0: how to train your own model. _Nature methods_, 19(12):1634–1641, 2022.
* Version 1: Carsen Stringer, Tim Wang, Michalis Michaelos, and Marius Pachitariu. Cellpose: a generalist algorithm for cellular segmentation. _Nature methods_, 18(1):100–106, 2021.
