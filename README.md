# cvdebug

A simple utility for displaying and debugging OpenCV images with matplotlib.

## Features

- Easily display OpenCV images with automatic BGR→RGB conversion
- Global `show()` function for quick image visualization
- Support for single-channel and multi-channel images
- Optional figure and axes return for custom annotations

## Installation

```bash
pip install cvdebug
```

## Usage

```python
import cv2
import numpy as np
from cvdebug import show

# Load and display an image
img = cv2.imread('image.jpg')
show(img, title="My Image")

# For grayscale images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show(gray, cmap='gray')

# Get figure and axes for custom annotations
img = cv2.imread('image.jpg')
fig, ax = show(img, wait=False)
ax.text(10, 30, "Annotation", color='red')
plt.show()
```

The `show()` function can be added to Python builtins by calling `cvdebug.install()`, allowing you to use it without importing:

## Command Line Usage

After installing the package, you can use the command-line tool to quickly view images:

```bash
# Direct command-line usage
show image.jpg
```

The command-line entry point is defined in the project's pyproject.toml, making it accessible from anywhere once installed.
