import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture('/home/vuong/Videos/PreSchool/Lyu You Lin.mp4')
POSITION_LINE = 0.75
# Check if camera opened successfully
if cap.isOpened() is False:
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = 416
frame_height = 416
num_of_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("num_of_frame", num_of_frame)
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('/home/vuong/Videos/test.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))
index = 0
rotation = False
while True:
    index += 1
    print(index)
    if index == int(num_of_frame):
        break
    # cap.set(cv2.CAP_PROP_POS_FRAMES, index)
    ret, frame = cap.read()
    rows, cols ,channel = frame.shape
    frame = cv2.transpose(frame)
    # # cols-1 and rows-1 are the coordinate limits.
    # if rotation:
    #     M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), -90, 0.5)
    #     dst = cv2.warpAffine(frame, M, (cols, rows))
    #     frame = dst

    if ret is False:
        continue

    # Write the frame into the file 'output.avi'
    # line = [(0, int(POSITION_LINE * frame.shape[0])),
    #         (int(frame.shape[1]), int(POSITION_LINE * frame.shape[0]))]
    # # line = [(0, int(0.33 * image.shape[0])), (int(image.shape[1]), int(0.33 * image.shape[0]))]
    # cv2.line(frame, line[0], line[1], (0, 255, 255), 2)
    text = 'index_' + str(index)
    (H, W) = frame.shape[:2]
    cv2.putText(frame, text, (5, H - (H-30)),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # out.write(frame)
    # cv2.imwrite('cauvuot.jpg', frame)

    # Display the resulting frame
    # cv2.resize(frame, (frame_width, frame_height))
    cv2.imshow('frame', frame)
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Break the loop
    # else:
    #     break

    # When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()