# PROJECT 1 - Fundamentals of Computer Vision (FCV)

Augmentation system for CV ML algorithms.

## Prerequisites:

- Python and OpenCV installed on local computer;
- a test directory containing 5 images with various content (e.g. saved from web) of the size 640 x 480.

## Specification:
Using Python and OpenCV write a program that:
- Allows user to select a directory on local disk. (e.g. using tkinter library)
- Read all .jpg images from this directory and, for each of them, apply a set of predefined augmentation algorithms with a set of predefined parameters. (e.g. Rotation with +15 degree).
- The augmentation algorithms and corresponding parameters to be applied will be loaded when the program starts from a configuration file (plain text, xml etc.)
- The results of augmentation process will be saved on a new directory (output dir), having the same name with the original one plus the "_aug" suffix.
- Each augmented image will be saved in the output dir having the name of augmentation algorithm as suffix followed by an incremental number starting with "_1". 


## Author
[Botean Cătălin-Cristian](https://github.com/catalinbotean/), Master of ML (Machine Learning) student, UPT