import cv2
import numpy as np 

def preProcess(hands, img):
    x, w, h, y = 0, 0, 0, 0
    bg_size = 300  # Fixed size of the white background
    offset = 20
    if len(hands) == 2:
    # Get bounding box that contains both hands
        x1, y1, w1, h1 = hands[0]['bbox']
        x2, y2, w2, h2 = hands[1]['bbox']
        x, y = min(x1, x2), min(y1, y2)
        w, h = max(x1+w1, x2+w2) - x, max(y1+h1, y2+h2) - y
    
    elif len(hands) == 1:
        x,y,w,h = hands[0]['bbox']

    # x,y are top left corner coordinates whereas w and h are width and height respectively.


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

            return (background, x, y)

    return (np.zeros((bg_size, bg_size, 3), dtype=np.uint8), 0, 0)