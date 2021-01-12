import cv2
import imutils


def on_pos_video_trackbar(val):
    global vs, frame_index

    if val != frame_index:
        frame_index = val
        vs.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        print("Set Pos : ", val)


def mouse_callback(event, x, y, flags, param):
    global mouse_down
    global step

    if event == cv2.EVENT_LBUTTONDOWN:
        if mouse_down is False:
            mouse_down = True
            step = 0
        else:
            step += 1

    elif event == cv2.EVENT_LBUTTONUP and mouse_down:
        mouse_down = False


main_title_window = "VIDEO"
vs = cv2.VideoCapture('/home/vuong/Videos/VIDEOS/camera_sau.mp4')
num_of_frame = int(vs.get(cv2.CAP_PROP_FRAME_COUNT))
pos_slider_max = num_of_frame
cv2.namedWindow(main_title_window, cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback(main_title_window, mouse_callback)
cv2.createTrackbar('Position', main_title_window, 0, pos_slider_max, on_pos_video_trackbar)
if vs.isOpened() is False:
    print("Open video false")
    exit()
frame_index = 0
pre_frame_index = 2
while True:
    if frame_index != pre_frame_index + 1:
        vs.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    pre_frame_index = frame_index

    ret, frame_ori = vs.read()
    if not ret:
        break
    view_frame = imutils.resize(frame_ori, width=720)
    text = "Frame index : {}".format(frame_index)
    (H_ori, W_ori) = view_frame.shape[:2]
    cv2.putText(view_frame, text, (10, H_ori - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    frame_index += 1

    cv2.setTrackbarPos('Position', main_title_window, frame_index)

    cv2.imshow(main_title_window, view_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("d") or key == ord("D"):
        if frame_index < num_of_frame:
            frame_index += 2
        # print('frame_index', frame_index)
    elif key == ord("f") or key == ord("F"):
        if frame_index > 2:
            frame_index -= 4
    elif key == 32:
        while True:
            view_frame_help = imutils.resize(view_frame, width=720)
            cv2.imshow(main_title_window, view_frame_help)
            key = cv2.waitKey(0) & 0xFF
            if key == 32:
                break

    elif key == ord("q") or key == ord("Q"):
        break

vs.release()
cv2.destroyAllWindows()