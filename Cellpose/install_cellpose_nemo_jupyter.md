# Installing CellPose on the HPC Cluster (nemo)

To install CellPose to run properly on a Jupyter notebook on the HPC cluster (**nemo**), follow these steps:

> ⚠️ **Be sure to use a GPU node while installing!**

---

- Download the files `install_cellpose_0525.sh` and `Cellpose_GPU_Check.ipynb` to a folder on nemo
  
   (e.g., `labname/working/username/cellpose0525`).


- Open an OnDemand desktop session on a GPU node.



- Open a terminal window in OnDemand.



- Navigate in the terminal to the folder where you downloaded the files.



- Run the install script:

  ```bash
  ./install_cellpose_0525.sh
  ```



- Wait a few minutes for everything to install.  
  *If it installs suspiciously quickly, something likely went wrong.*



- After installation, open a Jupyter session on OnDemand on a GPU node.



- Open the notebook `Cellpose_GPU_Check.ipynb` from the folder where you saved it.



- Run the two cells. If both return `True`, CellPose is successfully installed.



## Demo Notebook

For a demonstration of running **Cellpose-SAM** on images, please see this notebook:

👉 *(Insert link or relative path here)*

---
