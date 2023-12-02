def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f"Folder '{name}' already exists.")

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import os

# Define the desired location to create the folders
base_path = "C:/Users/durve/OneDrive/Desktop/Major Project/Training_Dataset"

# Create folders for all capital letters from 'A' to 'Z' and numbers from 0 to 9
for char_code in range(ord('A'), ord('Z') + 1):
    char = chr(char_code)
    folder_name = char
    folder_path = os.path.join(base_path, folder_name)
    create_folder(folder_path)

for num_code in range(ord('1'), ord('9') + 1):
    num = chr(num_code)
    folder_name = num
    folder_path = os.path.join(base_path, folder_name)
    create_folder(folder_path)


# Preprocessing - 
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
bg_size = 300  # Fixed size of the white background
offset = 20
count = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img,1) #Flips the side of camera to show left on left side and right on right
    hands, img = detector.findHands(img)

    if hands:
        if len(hands) == 2:
            # Get bounding box that contains both hands
            x1, y1, w1, h1 = hands[0]['bbox']
            x2, y2, w2, h2 = hands[1]['bbox']
            x, y = min(x1, x2), min(y1, y2)
            w, h = max(x1+w1, x2+w2) - x, max(y1+h1, y2+h2) - y
        
        elif len(hands) == 1:
            x,y,w,h = hands[0]['bbox']

        # x,y are top left corner coordinates whereas w and z are width and height respectively.


        # Crops the original image to give only the bounding box area.
        imgCrop = img[y-offset: y + h+offset, x-offset:x+ w+offset]
        
        # Check if imgCrop has valid dimensions
        # imgCrop.shape[0] is height and imgCrop.shape[1] is width. Checks if width and height are greater than 0. When hand goes out of image box, 
        # height and width goes less than 0 and results in error.
        if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
            # Create white background of 300x300 pixels.
            background = np.zeros((bg_size, bg_size, 3), dtype=np.uint8)
            background.fill(255)

            # Calculate scaling factor and new dimensions for imgCrop. It is calculated by dividing the 300px by width 
            # and height and taking the minimum value.
            scale = min(bg_size / imgCrop.shape[0], bg_size / imgCrop.shape[1])
            # Scaling the image as per the factor.
            new_w, new_h = int(imgCrop.shape[1] * scale), int(imgCrop.shape[0] * scale)

            # Resize imgCrop and paste onto center of white background
            if new_h > 0 and new_w > 0: # Ensure that dimensions are non-zero that is if hands goes out of box then dimensions becomes negative.
                cv2.imshow('Bounding Box', imgCrop)
                imgCrop = cv2.resize(imgCrop, (new_w, new_h))

                # Getting the gap and then push forward by half to bring image in the centre
                x_offset = (bg_size - new_w) // 2
                y_offset = (bg_size - new_h) // 2

                # Pasting the cropped image on the centre of white backgroud created
                background[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = imgCrop

                cv2 .imshow("Processed Image", background)

    cv2.imshow("Original image", img)

    # Press escape key for quitting
    # The function waitkey will wait for 1 milisecond to take input from keyboard

    # add location where to store the captured dataset.
    folder_path = "C:/Users/durve/OneDrive/Desktop/Major Project/Training_Dataset"
    key = cv2.waitKey(1)
    if key >= ord('a') and key <= ord('z') or key >= ord('A') and key <= ord('Z') or key >= ord('1') and key <= ord('9'):
        # Construct the full path to save the image
        folder_name = chr(key).upper()
        print(f'Folder name {folder_name}')
        print(f'Folder path {folder_path}')
        folder_path_key = os.path.join(folder_path, folder_name)
        count += 1
        filename = f"{count}.jpg"
        image_path = os.path.join(folder_path_key, filename)
        # Save the image to disk
        cv2.imwrite(image_path, background)
        print(f"Image saved to {image_path}.")
    elif key == 27:  # Escape key
        break
    

cv2.destroyAllWindows()