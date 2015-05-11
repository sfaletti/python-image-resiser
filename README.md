# Image Resizer
Resizes images for responsive web design.

This is a small Python script to resize images. It is recursive and will scour all subdirectories looking for JPEG and PNG files. It uses Python Image Library to do the actual work, and assumes it's already installed. It uses Tkinter for the folder selection dialog.

The script runs through each directory, looking for image files. When it finds one, it creates scaled copies at various widths. It then saves each file with a '-size' addendum. I wrote it to process a bunch of images for a web project.

Enjoy.
