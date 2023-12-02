import cv2

# Open a video file or capture device
video_capture = cv2.VideoCapture(0)  # Replace 'your_video.mp4' with your video file

# Check if the video opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
start_time = cv2.getTickCount()

while True:

    frame_count += 1

end_time = cv2.getTickCount()
total_time = (end_time - start_time) / cv2.getTickFrequency()
fps = frame_count / total_time

print(f"Frames per second: {fps:.2f}")

# Release the video capture object
video_capture.release()
cv2.destroyAllWindows()
