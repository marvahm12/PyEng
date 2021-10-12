import cv2
import sys
import matplotlib.pyplot as plt

def count_cards(infile="cards.jpg", nogui=False):
    # Read the image
    image = cv2.imread(infile)

    #convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #blur it
    blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)

    # Run the Canny edge detector
    canny = cv2.Canny(blurred_image, 30, 100)
    contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image2 = image
    cv2.drawContours(image2, contours, -1, (0,255,0), 2)

    print("Number of objects found = ", len(contours))

    if nogui:
        cv2.imwrite('test_count_cards.png', image2)
        return len(contours)
    else:
        # Show both our images
        image = cv2.imread(infile)
        cv2.imwrite("Original_image.png", image)
        cv2.imwrite("Blurred_image.png", blurred_image)
        cv2.imwrite("Canny.png", canny)
        cv2.imwrite("objects_Found.png", image2)
        #cv2.waitKey(0)

if __name__ == "__main__":
    count_cards()
    plt.savefig('output/Original_image.png')
    plt.savefig('output/Blurred_image.png')
    plt.savefig('output/Canny.png')
    plt.savefig('output/objects_Found.png')