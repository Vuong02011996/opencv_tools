import cv2
import imutils

all_point = []
frame_index = 0
vs = cv2.VideoCapture('/home/vuong/Videos/VIDEOS/camera_sau.mp4')
w, h = 900, 500


def on_pos_video_trackbar(val):
    global vs, frame_index

    if val != frame_index:
        frame_index = val
        vs.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        print("Set Pos : ", val)


def mouse_callback(event, x, y, flags, param):
    global mouse_down
    global step

    mouse_down = False

    if event == cv2.EVENT_LBUTTONDOWN:
        if mouse_down is False:
            mouse_down = True
            step = 0
        else:
            step += 1

    elif event == cv2.EVENT_LBUTTONUP and mouse_down:
        mouse_down = False


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
    global image, frame_index, vs, all_point
    # load the image, clone it, and setup the mouse callback function

    ret, frame_ori = vs.read()

    image = cv2.resize(frame_ori, (w, h))
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
            all_point = []

        # if the 'c' key is pressed, break from the loop
        elif key == ord("q"):
            print('all_point:', all_point)
            break
    cv2.imwrite('image_ref_cam_sau.jpg', image)
    cv2.destroyAllWindows()

    main_title_window = "VIDEO"
    # vs = cv2.VideoCapture('/home/vuong/Videos/VIDEOS/camera_sau.mp4')
    num_of_frame = int(vs.get(cv2.CAP_PROP_FRAME_COUNT))
    pos_slider_max = num_of_frame
    cv2.namedWindow(main_title_window, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(main_title_window, mouse_callback)
    cv2.createTrackbar('Position', main_title_window, 0, pos_slider_max, on_pos_video_trackbar)
    if vs.isOpened() is False:
        print("Open video false")
        exit()

    stop = False
    pre_frame_index = 2
    while True:
        if frame_index != pre_frame_index + 1:
            vs.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        pre_frame_index = frame_index

        ret, frame_ori = vs.read()
        if not ret:
            break
        view_frame = cv2.resize(frame_ori, (w, h))
        text = "Frame index : {}".format(frame_index)
        (H_ori, W_ori) = view_frame.shape[:2]
        cv2.putText(view_frame, text, (10, H_ori - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        frame_index += 1

        cv2.setTrackbarPos('Position', main_title_window, frame_index)

        for i, point in enumerate(all_point):
            cv2.line(view_frame, point[0], point[1], (0, 255, 0), 2)

        cv2.imshow(main_title_window, view_frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 32:
            while True:
                cv2.imshow(main_title_window, view_frame)
                key = cv2.waitKey(0) & 0xFF
                if key == 32:
                    break

                if key == ord("q") or key == ord("Q"):
                    stop = True
                    break

        elif key == ord("q") or key == ord("Q"):
            break
        if stop:
            break

    vs.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
