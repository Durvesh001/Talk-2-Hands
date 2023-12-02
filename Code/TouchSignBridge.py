# # Attempt 1 - Normal Code 
# import cv2
# import numpy as np
# import time
# from cvzone.HandTrackingModule import HandDetector
# from cvzone.ClassificationModule import Classifier



# def preProcess(hands, img):
#     if len(hands) == 2:
#     # Get bounding box that contains both hands
#         x1, y1, w1, h1 = hands[0]['bbox']
#         x2, y2, w2, h2 = hands[1]['bbox']
#         x, y = min(x1, x2), min(y1, y2)
#         w, h = max(x1+w1, x2+w2) - x, max(y1+h1, y2+h2) - y
    
#     elif len(hands) == 1:
#         x,y,w,h = hands[0]['bbox']

#     # x,y are top left corner coordinates whereas w and z are width and height respectively.


#     # Crops the original image to give only the bounding box area.
#     imgCrop = img[y-offset: y + h+offset, x-offset:x+ w+offset]
    
#     # Check if imgCrop has valid dimensions
#     # imgCrop.shape[0] is height and imgCrop.shape[1] is width. Checks if width and height are greater than 0. When hand goes out of image box, 
#     # height and width goes less than 0 and results in error.
#     if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
#         # Create white background of 300x300 pixels.
#         background = np.zeros((bg_size, bg_size, 3), dtype=np.uint8)
#         background.fill(255)

#         # Calculate scaling factor and new dimensions for imgCrop. It is calculated by dividing the 300px by width 
#         # and height and taking the minimum value.
#         scale = min(bg_size / imgCrop.shape[0], bg_size / imgCrop.shape[1])
#         # Scaling the image as per the factor.
#         new_w, new_h = int(imgCrop.shape[1] * scale), int(imgCrop.shape[0] * scale)

#         # Resize imgCrop and paste onto center of white background
#         if new_h > 0 and new_w > 0: # Ensure that dimensions are non-zero that is if hands goes out of box then dimensions becomes negative.
#             cv2.imshow('Bounding Box', imgCrop)
#             imgCrop = cv2.resize(imgCrop, (new_w, new_h))

#             # Getting the gap and then push forward by half to bring image in the centre
#             x_offset = (bg_size - new_w) // 2
#             y_offset = (bg_size - new_h) // 2

#             # Pasting the cropped image on the centre of white backgroud created
#             background[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = imgCrop

#             return (background, x, y)

#     return (np.zeros((bg_size, bg_size, 3), dtype=np.uint8), 0, 0)




# cap = cv2.VideoCapture(0)
# detector = HandDetector(maxHands=2)
# classifier = Classifier("C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/keras_model.h5", "C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/labels.txt")
# bg_size = 300  # Fixed size of the white background
# offset = 20

# labels = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F','Evening', 'G', 'H','Good', 'I', 'Hello','How are you?','J', 'K', 'L', 'M', 'N','Morning', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# while True:
#     success, img = cap.read()
#     img_Output = img.copy()
#     img = cv2.flip(img,1) #Flips the side of camera to show left on left side and right on right
#     hands, img = detector.findHands(img)

#     if hands:
#         background, x, y = preProcess(hands, img)
#         prediction, index = classifier.getPrediction(background)
#         cv2.putText(img_Output, labels[index], (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 0, 255), thickness=4, lineType=cv2.LINE_AA)
#         print(f'Label_Index = {index} and Value = {labels[index]}')
#         cv2.imshow('Original image', img_Output)

#     key = cv2.waitKey(1)
#     if key == 27: break
# cv2.destroyAllWindows()

# def frames():
#     # Initialize variables for FPS calculation
#     frame_count = 0
#     start_time = time.time()

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         # Process the frame here (e.g., display or analyze it)

#         # Increment the frame count
#         frame_count += 1

#         # Calculate elapsed time
#         elapsed_time = time.time() - start_time

#         # Calculate FPS
#         if elapsed_time >= 1.0:
#             fps = frame_count / elapsed_time
#             print("FPS:", fps)
#             # Reset the frame count and start time for the next measurement
#             frame_count = 0
#             start_time = time.time()

#         # Display the frame
#         cv2.imshow('Frame', frame)
        
#         # Break the loop if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and close OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()


# # Attempt 1 - Making a sentence out of predictions 
# import cv2
# import numpy as np
# import time
# from cvzone.HandTrackingModule import HandDetector
# from cvzone.ClassificationModule import Classifier



# def preProcess(hands, img):
#     if len(hands) == 2:
#     # Get bounding box that contains both hands
#         x1, y1, w1, h1 = hands[0]['bbox']
#         x2, y2, w2, h2 = hands[1]['bbox']
#         x, y = min(x1, x2), min(y1, y2)
#         w, h = max(x1+w1, x2+w2) - x, max(y1+h1, y2+h2) - y
    
#     elif len(hands) == 1:
#         x,y,w,h = hands[0]['bbox']

#     # x,y are top left corner coordinates whereas w and z are width and height respectively.


#     # Crops the original image to give only the bounding box area.
#     imgCrop = img[y-offset: y + h+offset, x-offset:x+ w+offset]
    
#     # Check if imgCrop has valid dimensions
#     # imgCrop.shape[0] is height and imgCrop.shape[1] is width. Checks if width and height are greater than 0. When hand goes out of image box, 
#     # height and width goes less than 0 and results in error.
#     if imgCrop.shape[0] > 0 and imgCrop.shape[1] > 0:
#         # Create white background of 300x300 pixels.
#         background = np.zeros((bg_size, bg_size, 3), dtype=np.uint8)
#         background.fill(255)

#         # Calculate scaling factor and new dimensions for imgCrop. It is calculated by dividing the 300px by width 
#         # and height and taking the minimum value.
#         scale = min(bg_size / imgCrop.shape[0], bg_size / imgCrop.shape[1])
#         # Scaling the image as per the factor.
#         new_w, new_h = int(imgCrop.shape[1] * scale), int(imgCrop.shape[0] * scale)

#         # Resize imgCrop and paste onto center of white background
#         if new_h > 0 and new_w > 0: # Ensure that dimensions are non-zero that is if hands goes out of box then dimensions becomes negative.
#             cv2.imshow('Bounding Box', imgCrop)
#             imgCrop = cv2.resize(imgCrop, (new_w, new_h))

#             # Getting the gap and then push forward by half to bring image in the centre
#             x_offset = (bg_size - new_w) // 2
#             y_offset = (bg_size - new_h) // 2

#             # Pasting the cropped image on the centre of white backgroud created
#             background[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = imgCrop

#             return (background, x, y)

#     return (np.zeros((bg_size, bg_size, 3), dtype=np.uint8), 0, 0)



# # Attempt 2 - Making a sentence out of predictions  
import cv2
import numpy as np
import time
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from gtts import gTTS


def waitTime(x):
    start = time.time()
    while time.time() - start < x:
        pass
    
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx START xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def preProcess(hands, img):
    x, w, h, y = 0, 0, 0, 0
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
            y_offset = (bg_size - new_h) // 24

            # Pasting the cropped image on the centre of white backgroud created
            background[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = imgCrop

            return (background, x, y)

    return (np.zeros((bg_size, bg_size, 3), dtype=np.uint8), 0, 0)


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

# Add your model's and label's location respectively.
classifier = Classifier("C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/keras_model.h5", "C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/labels.txt")
bg_size = 300  # Fixed size of the white background
offset = 20
start_time = time.time()
Final = []
language = 'en'

labels = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F','Evening', 'G', 'H','Good', 'I', 'Hello','How are you?','J', 'K', 'L', 'M', 'N','Morning', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listPredict = {}

firstTime = True

while True:
    success, img = cap.read()
    img_Output = img.copy()
    img = cv2.flip(img,1) #Flips the side of camera to show left on left side and right on right
    hands, img = detector.findHands(img)

    if hands:
        if firstTime:
            # Waiting for 5 seconds to start window and get ready for everything.
            waitTime(5)
            firstTime = False
            
        background, x, y = preProcess(hands, img)
        prediction, index = classifier.getPrediction(background)

        elapsed_time = time.time() - start_time

        listPredict[index] = 1 if index not in listPredict else listPredict[index] + 1

        if elapsed_time >= 5:
            maxValue = max(listPredict.values())
            for key in listPredict:
                if listPredict[key] == maxValue:
                    Final.append(labels[key])
                    listPredict = {}
                    print("######################### New #########################\n######################### New #########################\n######################### New #########################")
                    start_time = time.time()
                    break



        cv2.putText(img_Output, labels[index], (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 0, 255), thickness=4, lineType=cv2.LINE_AA)
        print(f'Label_Index = {index} and Value = {labels[index]}')
        cv2.imshow('Original image', img_Output)

    key = cv2.waitKey(1)
    if key == 27: break
cv2.destroyAllWindows()

sentence = ' '.join(Final[:])
print(sentence)

speech = gTTS(text=sentence, lang=language, slow=False)

speech.save('text2speech.mp3')