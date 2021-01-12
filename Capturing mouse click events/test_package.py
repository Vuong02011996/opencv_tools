# import the necessary packages
import cv2
import argparse

# now let's initialize the list of reference point
ref_point = []


def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point, crop

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        # print('ref_point1', ref_point)

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))
        print('ref_point2', ref_point)

        # draw a rectangle around the region of interest
        # cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.line(image, ref_point[0], ref_point[1], (0, 255, 0), 2)

        cv2.imshow("image", image)


def main():
    global image
    # load the image, clone it, and setup the mouse callback function
    image = cv2.imread('cauvuot.jpg')
    image = cv2.resize(image, (1280, 720))
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", shape_selection)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        # press 'r' to reset the window
        if key == ord("r"):
            image = clone.copy()

        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break

    # close all open windows
    cv2.destroyAllWindows()


def test():
    image = cv2.imread('cauvuot.jpg')
    clone = image.copy()
    cv2.namedWindow("image")
    text = 'Json data { "region": [[10, 954, 862, 988, 894, 640, 488, 616], [988, 984, 1882, 980, 1412, 648, 958, 640], [882, 856], [272, 822], [972, 852], [1636, 860]] }'
    cv2.putText(image, text, (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    p1 = (10, 954)
    p2 = (862, 988)
    p3 = (894, 640)
    p4 = (488, 616)
    p5 = (882, 856)
    p6 = (272, 822)

    cv2.line(image, p1, p2, (255, 0, 0), 1)
    cv2.putText(image, str(p1), p1, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.putText(image, str(p2), p2, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.line(image, p3, p4, (0, 255, 0), 2)
    cv2.putText(image, str(p3), (800, 640), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.putText(image, str(p4), p4, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.line(image, p5, p6, (0, 0, 255), 3)
    cv2.putText(image, str(p5), (800, 856), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.putText(image, str(p6), p6, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.line(image, p1, p4, (0, 255, 255), 1)
    cv2.line(image, p2, p3, (0, 255, 255), 1)
    # cv2.putText(image, text, (10, H - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    # image = cv2.resize(image, (1280, 720))

    p1 = (988, 984)
    p2 = (1882, 980)
    p3 = (1412, 648)
    p4 = (958, 640)
    p5 = (972, 852)
    p6 = (1636, 860)
    cv2.line(image, p1, p2, (255, 0, 0), 1)
    cv2.putText(image, str(p1), p1, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.putText(image, str(p2), (1800, 980), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.line(image, p3, p4, (0, 255, 0), 2)
    cv2.putText(image, str(p3), p3, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.putText(image, str(p4), p4, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.line(image, p5, p6, (0, 0, 255), 3)
    cv2.putText(image, str(p5), p5, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.putText(image, str(p6), p6, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)
    cv2.line(image, p1, p4, (0, 255, 255), 1)
    cv2.line(image, p2, p3, (0, 255, 255), 1)
    cv2.imwrite('tested.jpg', image)

    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        # press 'r' to reset the window
        if key == ord("r"):
            image = clone.copy()

        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break

        # close all open windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # test()
    main()