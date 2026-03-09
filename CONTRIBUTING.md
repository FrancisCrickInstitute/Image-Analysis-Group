# Contributing to Image-Analysis-Group

Thank you for your interest in improving these resources! This repository is maintained by the CALM (Advanced Light Microscopy) team at the Francis Crick Institute, and contributions from the community are welcome.

---

## What You Can Contribute

- Fix typos, broken links, or unclear instructions
- Add or improve troubleshooting sections
- Update installation steps when software versions change
- Add new guides for image analysis tools used at the Crick

---

## How to Submit a Contribution

1. **Fork** this repository to your own GitHub account.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/Image-Analysis-Group.git
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b fix/short-description-of-change
   ```
4. **Make your changes** — see the guidelines below.
5. **Commit** with a clear, descriptive message:
   ```bash
   git commit -m "Fix broken link in QuPath readme"
   ```
6. **Push** your branch and open a **Pull Request** against `master`.

---

## Writing Guidelines

- Write in plain, accessible English — these guides are read by researchers, not necessarily software engineers.
- Use consistent Markdown formatting with the rest of the file you're editing.
- For installation steps, number each step clearly and include exact commands in code blocks.
- If referencing Crick-internal resources (Intranet, PPMS, Slack), note that they are internal-only so external readers are not confused.
- Keep screenshots up to date — if you add a screenshot, place it in the `assets/` folder.

---

## What Not to Change

- Do not modify example pipeline files, training data, or notebooks without consulting the CALM team first.
- Do not remove links to internal Crick resources — they are valid for the primary audience.

---

## Questions?

If you are unsure whether a change is appropriate, reach out before opening a PR:

- **Email:** bioimage-analysis@crick.ac.uk
- **Slack (Crick staff):** #image-analysis
