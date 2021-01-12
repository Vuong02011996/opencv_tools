import cv2

all_point = []


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
        all_point.append(ref_point)
        # draw a rectangle around the region of interest
        # cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.line(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


def main():
    global image
    # load the image, clone it, and setup the mouse callback function

    vs = cv2.VideoCapture('/home/vuong/Videos/VIDEOS/camera_sau.mp4')
    ret, frame_ori = vs.read()

    image = cv2.resize(frame_ori, (1280, 720))
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
        elif key == ord("q"):
            print('all_point:', all_point)
            break

    # close all open windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
