import time, cv2
# Initialize variables for FPS calculation
frame_count = 0
start_time = time.time()
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Process the frame here (e.g., display or analyze it)

    # Increment the frame count
    frame_count += 1

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Calculate FPS
    if elapsed_time >= 1.0:
        fps = frame_count / elapsed_time
        print("FPS:", fps)
        # Reset the frame count and start time for the next measurement
        frame_count = 0
        start_time = time.time()

    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        