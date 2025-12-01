#!/bin/bash
. ~/.bashrc
echo "Let's install CellPose!!"
echo "This installs a conda environment called cellpose_env_0525 as this was last modified in May 2025 by Todd"
echo "Loading Anaconda"
ml Anaconda3
# if conda hasn't been setup do conda init or source the following script.
# this modifies your bashrc by removing existing conda initializations and
# reinitializes with the version of the loaded module
conda deactivate
#source /camp/apps/eb/software/Anaconda/conda.env.sh 
echo "Creating environment"
conda create --name cellpose_env_0525 python=3.11 -y
ml purge 
conda activate cellpose_env_0525
echo "installing cellpose"
pip install cellpose
echo "installing scikit-image"
pip install scikit-image
echo "installing numpy"
pip install numpy
echo "installing pandas"
pip install pandas
echo "Installing remote ikernel"
pip install remote_ikernel
python -m ipykernel install --user --name=cellpose_env_0525
echo "Setting up juypter"
python3 -m remote_ikernel manage --add --kernel_cmd="ml purge && ml cuDNN/8.4.1.50-CUDA-11.7.0 && conda activate cellpose_env_0525 && ipython3 kernel -f {connection_file}" --name="cellpose_env_0525" --interface=local --workdir="~/"--language=python3
echo "Whoo hoo! I've finished installing!"