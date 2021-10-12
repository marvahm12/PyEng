import cv2
import sys
import matplotlib.pyplot as plt


def display(infile):
    image = cv2.imread(infile)
    cv2.imwrite("Image.png", image)

if __name__ == "__main__":
    # Read the image. The first command line argument is the image

    display(sys.argv[1])
    plt.savefig('output/Image.png')
