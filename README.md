
# Pyxel Example: Using `pyxel.blt`

This project demonstrates how to use the `pyxel.blt` function to draw images or parts of images on the screen using the Pyxel library.

## Overview

The `pyxel.blt` function is used to draw an image or a part of an image on the screen. Here is a detailed explanation of the parameters and how it works in relation to loaded resources.

### Parameters of `pyxel.blt`

The function signature of `pyxel.blt` is:

```python
pyxel.blt(x, y, img, u, v, w, h, [colkey])
```

- **x, y**: Destination coordinates on the screen where the image will be drawn.
- **img**: Index of the source image in the Pyxel image bank. Typically, images are loaded into banks with indices like 0, 1, 2, etc.
- **u, v**: Coordinates of the top-left corner of the area of the source image you want to draw.
- **w, h**: Width (w) and height (h) of the area of the source image you want to draw.
- **colkey** (optional): Color key for transparency. Pixels of this color will not be drawn, allowing you to create images with transparent areas. If this parameter is omitted, no color will be considered transparent.

## Example Usage

Suppose you have an image loaded with index 0, and you want to draw a part of this image on the screen.

### Code

```python
import pyxel

# Initialize Pyxel with a window of 256x256 pixels
pyxel.init(256, 256)

# Load an image into the image bank 0
pyxel.load("my_resource.pyxres")

def update():
    pass

def draw():
    # Clear the screen with color 0 (usually black)
    pyxel.cls(0)
    
    # Draw a part of the image from bank 0 at position (50, 50) on the screen
    # with the source image area defined by the coordinates (0, 0) and dimensions (16, 16)
    pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)

# Run the Pyxel application
pyxel.run(update, draw)
```

In this example:

- `pyxel.init(256, 256)` initializes a window of 256x256 pixels.
- `pyxel.load("my_resource.pyxres")` loads resources (images, sounds, etc.) from the file `my_resource.pyxres`.
- `pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)` draws a 16x16 pixels portion of the image located at coordinates (0, 0) of the image in bank 0 to the position (50, 50) on the screen. The color key 0 is used for transparency, meaning that all pixels of color 0 in the source image will not be drawn.

In summary, `pyxel.blt` is a powerful function to draw specific parts of images onto the screen, allowing for various graphic effects and precision based on loaded resources.
