# Talk-2-Hands
## Project Description:
Successfully developed and implemented a cutting-edge project named 'Talk 2 Hands,' focused on converting Indian Sign Language to text using advanced Machine Learning techniques. Our project entailed writing a comprehensive codebase, which incorporated key libraries such as OS, cvzone's Hand Tracking and Classifier Module, cv2, and numpy. Leveraging Transfer Learning on CNN, we meticulously trained a model utilizing Google Teachable Machine, using an extensive dataset of approximately 21,000 diverse sign language images. The primary objective of our project was to bridge the communication gap by accurately translating Indian Sign Language into text, thereby empowering individuals with hearing impairments. To achieve this, we adopted a rigorous training approach, enabling our model to achieve exceptional performance. The testing phase yielded an impressive accuracy rate of 80%, while our training accuracy reached a remarkable 97%.
To ensure the robustness and reliability of our solution, we meticulously curated a comprehensive testing dataset comprising 9,000 images representative of real-world sign language gestures. Through diligent training and testing, we validated the effectiveness of our approach and exhibited the potential for accurate and efficient sign language translation. By undertaking this project, we demonstrated our team's technical proficiency in handling complex challenges, applying advanced ML techniques, and utilizing libraries effectively. The Talk 2 Hands project stands as a testament to our dedication to innovation, accessibility, and inclusivity.

## Following are the steps followed for making this project - 
1. 'data_collection.py' - code continuously tracks hands in video frames, extracts the hand region, and processes the hand images by resizing and pasting them onto a white background. The user can save the processed images into separate folders by pressing the corresponding keys on the keyboard. Following image is an example of how it is captured for data collection -
   
![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/62113e54-449e-4755-80f4-79fa7bf2697d)


2. 'Liveaction.py' - code demonstrates real-time sign language recognition by capturing video frames, detecting hands, processing the hand region, and classifying the sign language gesture using a pre-trained model. The predicted label is then displayed on the screen, enabling communication accessibility for individuals using sign language. Following is the example of prediction by the model -

![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/f8a0eb2b-a269-45a9-99f3-acdca8412dfc)


3. 'accuracy.py' - code calculates the accuracy of the training and testing dataset.

## Model Accuracy -
1. Training Accuracy -
![WhatsApp Image 2023-07-18 at 12 44 53](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/8508590b-085e-42e6-9d7b-91f519b8f710)


2. Testing Accuracy - 
![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/d0f635f8-de3a-4ca8-8687-012e029a8be0)


3. Following image shows sign along with its Prediction Accuracy - 
![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/ff9ca519-c278-463d-ad05-1453cbe6ee5c)





The project enables the conversion of Indian Sign Language to text using machine learning techniques. Trained the model with an extensive dataset of approximately 21,000 images, resulting in an impressive testing accuracy of 80% and a training accuracy of 97%. Demonstrated the potential for accurate and efficient translation of sign language to enhance communication accessibility.
