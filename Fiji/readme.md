# Installing FIJI on OnDemand
[FIJI](https://imagej.net/software/fiji/) (*FIji Is Just ImageJ*) is pre-installed on NEMO, but the shared version does **not allow plugin installation**.
If you need to install plugins or customise FIJI for your analysis, follow these steps to install your own version.

More information about how to access OnDemand at the Crick can be found in the [Crick HPC Wiki](https://wiki.thecrick.org/display/HPC/OnDemand).
<br><br>
> ⚠️ **NOTE – you'll only need to run these instructions once. Afterwards, the software will be saved in your NEMO storage**.

---

## ⚠️ Before You Start
Your home directory has very **limited storage**, so FIJI should **not** be installed there directly.

Instead, you should **softlink your home working directory** into your **lab** or **STP** shared space (which has much more storage).

If this hasn’t been done yet (or you're unsure), please contact the **HPC team** via the `#hpc` Slack channel — they can help you set this up.

---
## Step 1: Open an OnDemand Desktop and Launch a Terminal
1. Start a new OnDemand Desktop session. Select `Xfce` as your Desktop Environment and `ncpu` partition.
You can find detailed instructions here:
[Crick OnDemand Documentation](https://wiki.thecrick.org/display/HPC/OnDemand)
![NEMO Desktop options](https://github.com/FrancisCrickInstitute/Image-Analysis-Group/blob/master/assets/OD-desktop-env-partition-screenshot.png)

2. Once your desktop session starts, **right-click** anywhere on the desktop and select *"Open Terminal Here"*, or click the **Terminal icon** at the bottom of the desktop.

![Open Terminal Screenshot](https://github.com/FrancisCrickInstitute/Image-Analysis-Group/blob/master/assets/open-terminal-xfce-od-screenshot.png)

---

## Step 2. Download the Installer
1. Go to the folder on NEMO where you want to install FIJI.
Example:
```bash
cd /nemo/home/your-user-name/working/your-user-name/software/
```
2. Download the FIJI installation script by clicking the link below:
 👉 [install_FIJI_w_download.sh](https://github.com/FrancisCrickInstitute/CALM/blob/master/Fiji/install_FIJI_w_download.sh)

---

## Step 3. Run the Installer

In your OnDemand terminal:

1. Navigate to the folder where you downloaded the installer:
```bash
cd /nemo/home/your-user-name/working/your-user-name/software/
   ```
2. Run the installation script:
   ```bash
   ./install_FIJI_w_download.sh
   ```

This will:
- Download the latest FIJI version
- Unzip and set it up in the current directory
- Create a launcher script called `Run_Fiji.sh` in your **home directory**

---

## Step 4. Launch FIJI
After installation:
1. Open a **new terminal**
2. Run:
3. ```bash
   ./Run_Fiji.sh
   ```

FIJI should now open and be ready to use 🎉

---

## Useful Notes

- To open FIJI later, simply start and OnDemand Desktop, open a terminal, and run:
```bash
   ./Run_Fiji.sh
   ```
- You can install plugins, update FIJI, and customise settings. The changes will now be done on this copy of FIJI that lives in your NEMO storage.
- If you encounter permission or storage issues, reach out to the **HPC team** via the `#hpc` Slack channel.
