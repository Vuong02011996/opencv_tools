import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture('/home/vuong/Videos/VIDEOS/crop3_head_track.mp4')
POSITION_LINE = 0.75
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
num_of_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('/home/vuong/Videos/VIDEOS/crop3_head_track_frame_index.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))
index = 0
while (True):
    index += 1
    # cap.set(cv2.CAP_PROP_POS_FRAMES, index)
    ret, frame = cap.read()

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
    out.write(frame)
    # cv2.imwrite('cauvuot.jpg', frame)

    # Display the resulting frame
    # cv2.imshow('frame', frame)

    print(index)
    if index == int(num_of_frame):
        break

    # Press Q on keyboard to stop recording
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    # Break the loop
    # else:
    #     break

    # When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()