# drcnn-src
Title
Detection of Diabetic Retinopathy using Convolutional Neural Network 



Steps to use the CLI -

Clone the repository from github

Install the dependencies from the requirements.txt document.

Run pre_processing.py on the new image for blood vessel segmentation.

Open main.py and change the variables according to the working directory on line 137 - 141.

Run main.py with the desired argument.

Arguments for command line -

-h -> To get help for the CLI

-a, --all -> Run the analysis on all the validation images and print CONFUSION MATRIX and ACCURACY

-i, --image -> Run the analysis on one image, name to be given as the second argument.

Example -
python3.6 main.py -i image.png
