# Attempt 4
from cvzone.ClassificationModule import Classifier
import cv2
import os

labels = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F','Evening', 'G', 'H','Good', 'I', 'Hello','How are you','J', 'K', 'L', 'M', 'N','Morning', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
classifier = Classifier("C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/keras_model.h5", "C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/labels.txt")
accuracy = []
accuracy_dic = {}

for x in labels:
    img_path = f"C:/Users/durve/OneDrive/Desktop/Major Project/Training_Dataset/{x}"
    
    # Making list of all the images at the directory (variable - image_path)
    files = os.listdir(img_path) 
    ryt_count = 0
    total = len(files)
    for i, file in enumerate(files):
        img_file = os.path.join(img_path, file)
        try:
            img = cv2.imread(img_file)
            prediction, index = classifier.getPrediction(img)
            if labels[index] == x:
                ryt_count += 1
                
        except Exception as e:
            print(f"Error loading image {img_file}: {e}")
            continue

    perc = ((ryt_count)/total)*100
    print(f'Accuracy for {x} is {perc:.3f}%')
    accuracy.append(round(perc,3))

print(f"Overall accuracy: {sum(accuracy)/len(accuracy):.3f}%")
print(f'Accuracy List = {accuracy}')

for i in range(len(accuracy)):
    accuracy_dic[labels[i]] = accuracy[i]

print(f"Accuracy_dic = {accuracy_dic}")