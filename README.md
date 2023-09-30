# 3d print errors detect

This is an algorithm for detecting errors in 3D prints developed to identify common issues such as spaghetti, tying, and pimples.

## Description

3D prints can be susceptible to a range of errors that affect the quality of the final result. This algorithm employs computer vision techniques to analyze an image of the 3D print and identify the following types of errors:

1. **Spaghetti**: This error occurs when the melted filament from the printer is not properly deposited, resulting in a messy appearance with thin, disorderly threads.

2. **Tying**: Tying refers to areas where the filament accumulates or becomes excessively connected, often due to high print speeds or improper settings.

3. **Pimples**: Pimples are small protrusions that appear on the surface of the print, typically caused by minor variations in temperature or filament extrusion.

## Requirements

To use this algorithm, you will need the following dependencies:

- Python 3.11
- Computer vision libraries like OpenCV

## How to Use

1. Clone this repository to your machine:
```
git clone https://github.com/your-username/3d_print_errors_detect.git
```
2. Install the necessary dependencies:
```
pip install -r requirements.txt
```
