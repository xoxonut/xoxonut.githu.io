# Frank Hui — CV

A dependency-free, responsive CV site for GitHub Pages. The page uses a compact resume layout with a print stylesheet for clean A4 or Letter PDF export.

Preview it locally with the included server:

```bash
python3 preview_server.py --open
```

Then visit `http://localhost:8000/`. The server serves only this repository, disables browser caching for quick edits, and stops with `Ctrl+C`.

## Customize it

The CV content lives in `index.html`. Update the copy, contact links, and section entries there as the CV changes. The visual system is in `styles.css`, with responsive typography, keyboard focus styles, reduced-motion support, and print-specific spacing.

## Print or export to PDF

Open the browser print dialog and choose **Save to PDF**. The result uses the resume’s compact print layout.

## GitHub Pages

In the repository settings, set Pages to deploy from the branch containing these files and use the repository root as the folder. No build command is required.
