# Cellpose

**Cellpose** is a general purpose, deep learning-based segmentation algorithm for biological images ([Cellpose on GitHub](https://github.com/MouseLand/cellpose)).

This folder contains guides and resources to help you use Cellpose on the Crick's HPC cluster, with and without Jupyter notebooks, plus demo data and example notebooks.

---

## Getting Started

1. **Choose your installation method:**
- Want to use Cellpose in a Jupyter notebook on the cluster?
  👉 Follow [these instructions](./install_cellpose_nemo_jupyter.md).
- Want to run Cellpose from FIJI or as a GUI in an OnDemand Desktop session (without Jupyter notebooks)?
  👉 See [these instructions](./Run_Cellpose_From_FIJI_on_OnDemand.md).
> ⚠️ **Be sure to use a GPU node while installing on the HPC cluster (nemo)!**

2. **Try the Example Notebook:**
  - **[Cellpose GPU Check Notebook](./Cellpose_GPU_Check.ipynb):**  
     *Quickly verify your Cellpose installation and GPU access.*
  - **[Crick Cellpose-SAM Demo Notebook](./Crick_CellPose_SAM.ipynb):** <br>
     *Step-by-step guide to segmenting images with Cellpose-SAM on Nemo. Works with 2D images.*

3. **Download Demo Images:** <br>
   *Try out Cellpose using our [demo images](./demo_images/).*

---

## File & Folder Overview

- **demo_images/**  
  Example images to try with Cellpose.

- **Cellpose_GPU_Check.ipynb**  
  Jupyter notebook for testing your Cellpose install and GPU setup.

- **Crick_CellPose_SAM.ipynb**  
  Full workflow notebook for segmenting images with Cellpose-SAM.  

- **install_cellpose_nemo_jupyter.md**  
  Step-by-step guide to installing Cellpose in a JupyterLab environment on Nemo.

- **Run_Cellpose_From_FIJI_on_OnDemand.md**  
  Guide to installing Cellpose for use from an OnDemand desktop session, including FIJI integration.

- **install_cellpose_0525.sh**  
  Shell script for setting up the Cellpose environment.

---

## ❓ Need Help?
**Issues or questions about the install? 3D images? Advanced workflows?:** <br>
The provided notebooks are for 2D images. For 3D support, or further help, contact Todd, Dave, or Sara from CALM.

---

_Last updated: May 2025_
