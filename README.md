# TouchSign Bridge
## Project Description:
Our project, 'TouchSign Bridge,' revolutionizes communication by translating Indian Sign Language into text using cutting-edge Machine Learning techniques within a web application. To achieve this, we developed a robust codebase utilizing pivotal libraries such as OS, cvzone, cv2, and numpy, while implementing Transfer Learning on a CNN through Google Teachable Machine. This model was meticulously trained on a diverse dataset comprising 21,000 sign language images to ensure accurate translation (the code to capture dataset is included in the files). To achieve this, we adopted a rigorous training approach, enabling our model to achieve exceptional performance. The testing phase yielded an impressive accuracy rate of 80%, while our training accuracy reached a remarkable 97%.
   The project leveraged ReactJS for the frontend and Flask for the backend. Input from the frontend was processed on the backend, where the image frame was analyzed and predictions were made. The output, generated text, was sent back to the frontend for display. To ensure accuracy, within a time frame of 5 seconds (150 frames at 30fps), the most frequently predicted sign was considered as the correct output.
   The generated text was further converted into audio using the gTTS Python library. Subsequently, this text was sent back to the backend for conversion into Braille. The resulting Braille output was then displayed on the frontend screen, completing the transformation of sign language into accessible text, audio, and Braille formats.
   The Talk 2 Hands project showcases our team's technical prowess in implementing ReactJS and Flask, handling complex ML challenges, and integrating various libraries to create an innovative solution. It stands as a testament to our commitment to inclusivity and accessibility, empowering individuals with hearing impairments through technology.

## Following are the steps followed for making this project - 
1. Frontend built using ReactJs -
   ![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/96a95b80-1de7-4f2f-8494-c90fde1b0e41)

2. Text-2-Speech -
   ![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/d78a5010-3ba4-43aa-88c5-8ddec625e1a4)

3.  Text-2-Braille -
   ![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/b6053184-2a66-4c7b-b3de-d511b83337e8)

4. 'data_collection.py' - code continuously tracks hands in video frames, extracts the hand region, and processes the hand images by resizing and pasting them onto a white background. The user can save the processed images into separate folders by pressing the corresponding keys on the keyboard. Following image is an example of how it is captured for data collection -
![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/62113e54-449e-4755-80f4-79fa7bf2697d)

5. 'Liveaction.py' - code demonstrates real-time sign language recognition by capturing video frames, detecting hands, processing the hand region, and classifying the sign language gesture using a pre-trained model. The predicted label is then displayed on the screen, enabling communication accessibility for individuals using sign language. Following is the example of prediction by the model -
![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/f8a0eb2b-a269-45a9-99f3-acdca8412dfc)

6.  Sentence and audio formation -
   ![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/af8d8729-586d-4d72-bec9-a59e0fe0311d)

7. 'accuracy.py' - code calculates the accuracy of the training and testing dataset.
   
## Model Accuracy -
- Training Accuracy -
![WhatsApp Image 2023-07-18 at 12 44 53](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/8508590b-085e-42e6-9d7b-91f519b8f710)


- Testing Accuracy - 
![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/d0f635f8-de3a-4ca8-8687-012e029a8be0)


- Following image shows sign along with its Prediction Accuracy - 
![image](https://github.com/Durvesh001/Talk-2-Hands/assets/75305014/ff9ca519-c278-463d-ad05-1453cbe6ee5c)





The project enables the conversion of Indian Sign Language to text using machine learning techniques. Trained the model with an extensive dataset of approximately 21,000 images, resulting in an impressive testing accuracy of 80% and a training accuracy of 97%. Demonstrated the potential for accurate and efficient translation of sign language to enhance communication accessibility.
