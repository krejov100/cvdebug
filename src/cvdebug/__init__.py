import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys


def show(
    img: np.ndarray | None = None,
    title: str = "Image",
    cmap: str | None = None,
    wait: bool = True,
    block: bool = True,
):
    """
    Display an OpenCV image via matplotlib, auto-converting BGR→RGB.

    Args:
        img: H×W or H×W×3 array in BGR (if 3-channel) or gray.
        title: window title.
        cmap: matplotlib colormap (e.g. 'gray') for single-channel images.
        wait: if False, returns the fig & ax so you can overlay annotations.
    """
    if img is None:
        if len(sys.argv) < 2:
            print("No image provided")
            return
        img = cv2.imread(sys.argv[1])
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.axis("off")
    ax.imshow(img, cmap=cmap)
    if wait:
        plt.show(block=block)
    else:
        return fig, ax

def install():
    import builtins
    setattr(builtins, "show", show)
