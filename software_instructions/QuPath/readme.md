# Accessing QuPath 0.7.0 on the HPC Cluster

This guide will walk you through how to use **QuPath 0.7.0** on the Crick's HPC cluster. If you need help at any step, see the [support section](#need-help-contact-us).

This version of QuPath requires some libraries that are not compatible with NEMO's. To solve this, QuPath runs in a "container" – a self-contained environment that has everything it needs.
So rather than installing it ourselves, it is available in the _apps_ folder in NEMO. These instructions will guide you on how to access it. 

> **Looking for an older version?** Earlier guides are available for [QuPath 0.6](access_qupath_v6_nemo.md) and [QuPath 0.5.1](install_v051_HPC.md).

---

## Quick Navigation

- [What is QuPath 0.7.0?](#what-is-qupath-070)
- [Instructions to Access QuPath v0.7 with OnDemand](#instructions-to-access-qupath-v07-with-ondemand)
- [Shortcut: add the QuPath icon onto your NEMO Desktop](#shortcut-add-the-qupath-icon-onto-your-nemo-desktop)
- [How to Set Up Your User Directory](#how-to-set-up-your-user-directory)
- [Accessing OMERO from QuPath](#accessing-omero-from-qupath)
- [Accessing Your Data in QuPath](#accessing-your-data-in-qupath)
- [Need Help? Contact Us!](#need-help-contact-us)

---

## What is QuPath 0.7.0?
QuPath is a popular, open-source tool for digital pathology and whole slide imaging analysis. The new version (0.7.0) brings several new features and improvements.
To learn more about what's new, see:
[QuPath v0.7.0 release notes & features](https://github.com/qupath/qupath/blob/main/CHANGELOG.md#version-070)

---

## Instructions to Access QuPath v0.7 with OnDemand

### Step 1: Start a Desktop Session

1. Log in to the HPC cluster via [Open OnDemand](https://ondemand001.nemo.thecrick.org).
2. Start a **Nemo desktop session**. For more information, see the [HPC Wiki](https://wiki.thecrick.org/display/HPCuserwiki/High+Performance+Computing+%28HPC%29+user+wiki).

---

### Step 2: Open a Terminal

- Once your desktop session starts, open a **terminal window**.

![OnDemand open terminal screenshot](../../assets/open-terminal-xfce-od-screenshot.png)

---

### Step 3: Load the Singularity Module

Every time you open a new terminal, you must laod the Singularity module – the container platform.
Type the following and press Enter:

```bash
ml Singularity/3.11.3
```

---

### Step 4: Run QuPath

Replace `path/to/your/data` with the folder where your data, project, and images are stored.

**a) If you are using a GPU node:**

```bash
singularity run --nv -B /path/to/your/data:/data /camp/apps/containers/QuPath/0.7.0/qupath_0.7.0.sif
```

**b) If you are NOT using a GPU node:**

```bash
singularity run -B /path/to/your/data:/data /camp/apps/containers/QuPath/0.7.0/qupath_0.7.0.sif
```

**Important:**
- You must replace `/path/to/your/data` with the actual path to your data on the cluster (for example, `/camp/lab/labname`).
- Your data will be accessible inside QuPath at the `/data` folder.

---
## Shortcut: add the QuPath icon onto your NEMO Desktop
Every time you want to access the QuPath container via [OnDemand](https://ondemand001.nemo.thecrick.org/), you'll have to input the code in [Step 4](#step-4-run-qupath) above. To avoid interacting with the terminal every time, we can install a QuPath icon onto your NEMO Desktop (one time only!).

### Step 1: Start an Xfce session
Ensure you have "Xfce" selected when requesting a session in OnDemand. 
<p><img src="../../assets/ondemand_xfce_session_screenshot.png" width="50%" alt="OnDemand Xfce session screenshot"></p>

### Step 2: Open the terminal 
Once your desktop session starts, open a **terminal window**.
<p><img src="../../assets/open-terminal-xfce-od-screenshot.png" width="75%" alt="OnDemand Terminal screenshot"></p>

### Step 3: Open the text editor
We now need to create a little script that contains the commands run in the instructions above. Open the text editor (`nano`) and create a file named `run_qupath_v07.sh` by typing:
```bash
nano ~/run_qupath_v07.sh
```
and click Enter.

### Step 4: Input the commands to open QuPath
The _nano_ text editor will open a blank text file. Input the two lines of code that you normally type to open the QuPath container (see [Step 4](#step-4-run-qupath)). 
```bash
ml Singularity/3.11.3
singularity run --nv -B /path/to/your/data:/data /camp/apps/containers/QuPath/0.7.0/qupath_0.7.0.sif
```

> ⚠️: ensure that `path/to/your/data` is the location of your working directory inside your lab's NEMO space (e.g., `nemo/lab/labname/yourusername`. If you input a very specific folder, you will not be able to access anything _before_ that folder.

### Step 5: Save the new file
* Exit the text editor with '^X'.
* You will be prompted to select whether you want to save the file, type 'Y'.
* Then click Enter to save the .sh file with its current name.

### Step 6: Ensure the file was successfully created
List all the files in your home directory by typing:
```bash
ls ~
```
You should see a file named `run_qupath_v07.sh`.

### Step 7: Add execute permissions to the file
Now run:
```bash
chmod +x run_qupath_v07.sh 
```

Ensure that the file now appears in green when running:
```bash
ls ~
```

And check it opens QuPath successfully:
```bash
./run_qupath_v07.sh
```

### Step 8: Add the shortcut icon onto your Desktop
Right click anywhere in your Desktop, and select "Create Launcher".
<p><img src="../../assets/ondemand_create_launcher_screenshot.png" width="50%" alt="OnDemand create Launcher screenshot"></p>

* **Name**: "QuPath v0.7"
* **Command**: select the folder where `run_qupath_v07/sh` lives.
* **Icon** (optional): you can download the logo [here](./qupath_logo.png), add it somewhere in your NEMO storage, and select that folder in window finder.

<p><img src="../../assets/qupath_launcher_screenshot.png" width="25%" alt="QuPath Launcher screenshot"></p>


🎉 Click _Save_ and you should be all set! 🎉

---

## How to Set Up Your User Directory

> **First time only!**

The first time you open QuPath, you will be asked to select a **User Directory**.
- Please **create a new folder** (e.g., `qupath_v7`) inside your **lab-space directory** (not your home folder!).
-   - Example: `/camp/lab/labname/yourusername/qupath_v7`
- Select this folder as your User Directory.
**Why?** The home folder has limited space and can fill up quickly! Extensions and plugins are installed here, so choose a location with enough storage.

---

## Accessing OMERO from QuPath

**OMERO** is an image server available at the Crick to store and manage microscopy images. It is the recommended location for storing image data, and QuPath can access OMERO images directly via an extension. 

**To install the OMERO extension**:
Follow the installation instructions in the [Crick OMERO Guide](https://franciscrickinstitute.github.io/crick-omeroguide/qupath/docs/installation.html).

Once installed, you'll be able to browse and open your images directly from OMERO within QuPath, without needing to copy them locally.

---

## Accessing your data in QuPath

When you open a project/image or are selecting your user directory, a file browser window will appear. **Important**: this window opens in "Home" by default, so your home directory, but this is NOT where your data is located. 

Follow these steps to navigate to your data:

1. In the file browser, click on **"Other locations"** (on the left sidebar)
2. Select **"Computer"** to access the root file system.
3. Navigate to the **"data"** folder.
![QuPath data location](../../assets/qupath_v6_access_data.png)

4. You will now see the path you specified when launching QuPath in the terminal (step 4). For example, `/camp/lab/labname`.
From here, you can navigate to your project files.

**Note:** once you navigate into the `/data` folder, you won't be able to navigate backwards to other system locations, so make sure the `/path/to/your/data` includes all the folders you need to access in your QuPath project.

---

## Need Help? Contact Us!

If you have any questions or run into any issues, we're here to help. Reach out to the Image Analysis team in CALM:

- **Email**: [bioimage-analysis@crick.ac.uk](mailto:bioimage-analysis@crick.ac.uk)
- **Slack**: #image-analysis
 
Happy analysing!

---
