# Frank Hui — CV

A dependency-free, responsive CV site for GitHub Pages. The page uses a compact software-resume layout with a centered paper sheet on screen and a print stylesheet for clean A4 or Letter PDF export.

Open `index.html` directly in a browser, or serve the folder with any static web server. Use the section links at the top to navigate on screen; they are hidden when printing.

## Customize it

The CV content lives in `index.html`. Update the copy, contact links, and section entries there as the CV changes. The visual system is in `styles.css`, with an accent color, responsive stacking for narrow screens, keyboard focus styles, reduced-motion support, and print-specific spacing.

The current year in the footer is set by the small dependency-free script in `script.js`.

## Print or export to PDF

Open the browser print dialog and choose **Save to PDF**. Navigation, the back-to-top link, the page shadow, and the blue page background are removed automatically for a paper-friendly result.

## GitHub Pages

In the repository settings, set Pages to deploy from the branch containing these files and use the repository root as the folder. No build command is required.
