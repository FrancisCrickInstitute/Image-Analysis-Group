# Accessing QuPath 0.6.0 on the HPC Cluster

This guide will walk you through how to use **QuPath 0.6.0** on the Crick's HPC cluster. If you need help at any step, see [support section](#need-help-contact-us).

This version of QuPath requires some libraries that are not compatible with NEMO's. To solve this, QuPath runs in a "container" – a self-contained environment that has everything it needs.
So rather than installing it ourselves, it is available in the _apps_ folder in NEMO. These instructions will guide you on how to access it. 

---

## What is QuPath 0.6.0?
QuPath is a popular, open-source tool for digital pathology and whole slide imaging analysis. The new version (0.6.0) brings several new features and improvements.
To learn more about what's new, see:
[QuPath v0.6.0 release notes & features](https://forum.image.sc/t/qupath-v0-6-0-now-available/114104)

---

### Step 1: Start a Desktop Session

1. Log in to the HPC cluster via [Open OnDemand](https://ondemand.nemo.thecrick.org).
2. Start a **Nemo desktop session** with the resources you need (CPU/GPU, memory...).

---

### Step 2: Open a Terminal

- Once your desktop session starts, open a **terminal window**.

---

### Step 3: Load the Singularity Module

Every time you open a new terminal, you must laod the Singularity module – the container platform.
Type the following and press Enter:

```bash
ml Singularity/3.11.3
```

---

### Step 4: Run QuPath

Replace `path/to/your/data` with the folder where your data/project/images are stored.

**a) If you are using a GPU node:**

```bash
singularity run --nv -B /path/to/your/data:/data /camp/apps/containers/QuPath/0.6.0/qupath_0.6.0.sif
```

**b) If you are NOT using a GPU node:**

```bash
singularity run -B /path/to/your/data:/data /camp/apps/containers/QuPath/0.6.0/qupath_0.6.0.sif
```

**Important:**
- You must replace `/path/to/your/data` with the actual path to your data on the cluster (for example, `/camp/lab/labname/yourusername/proj-name`).
- Your data will be accessible inside QuPath at the `/data` folder.

---

### Step 5: First-Time Setup – Select Your User Directory

The first time you open QuPath, you will be asked to select a **User Directory**.
- Please **create a new folder** (e.g., `qupath_v6`) inside your **lab-space directory** (not your home folder!).
-   - Example: `/camp/lab/labname/yourusername/qupath_v6`
- Select this folder as your User Directory.
- **Why?** The home folder has limited space and can fill up quickly! Extensions and plugins are installed here, so choose a location with enough storage.

---

## Need Help? Contact Us!

If you have any questions or run into any issues, we're here to help. Reach out to the Image Analysis team in CALM:

- **Email**: [bioimage-analysis@crick.ac.uk](mailto:bioimage-analysis@crick.ac.uk)
- **Slack**:
  - Sara Salgueiro Torres
  - Dave Barry
 
Happy analysing!

---
