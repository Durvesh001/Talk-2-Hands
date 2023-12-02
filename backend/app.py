from flask import Flask, jsonify, request
from flask_cors import CORS  
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from preProcess import preProcess

app = Flask(__name__)
CORS(app)  

@app.route('/classify', methods=['POST'])
def classify():
    image_blob = request.files['image']
    nparr = np.fromstring(image_blob.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    detector = HandDetector(maxHands=2)
    classifier = Classifier("C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/keras_model.h5", "C:/Users/durve/OneDrive/Desktop/Major Project/Application/Model/labels.txt")

    labels = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F','Evening', 'G', 'H','Good', 'I', 'Hello','How are you?','J', 'K', 'L', 'M', 'N','Morning', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    background, x, y = preProcess(hands, img)

    prediction, index = classifier.getPrediction(background)
    print(f'Predicted Output - {labels[index]}')
    # return jsonify(f'Predicted Output is - {labels[index]}')
    return jsonify({'': labels[index]})



@app.route('/braille', methods=['POST'])
def braille():
    data = request.get_json()  # Get JSON data from the POST request
    input_text = data.get('text')  # Access the 'text' field from JSON
    braille_output = text_to_braille(input_text)
    print(braille_output)
    return jsonify(braille_output)

def text_to_braille(text):
    braille_dict = {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
        'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
        'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
        's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
        'y': '⠽', 'z': '⠵',
        'A': '⠠⠁', 'B': '⠠⠃', 'C': '⠠⠉', 'D': '⠠⠙', 'E': '⠠⠑', 'F': '⠠⠋',
        'G': '⠠⠛', 'H': '⠠⠓', 'I': '⠠⠊', 'J': '⠠⠚', 'K': '⠠⠅', 'L': '⠠⠇',
        'M': '⠠⠍', 'N': '⠠⠝', 'O': '⠠⠕', 'P': '⠠⠏', 'Q': '⠠⠟', 'R': '⠠⠗',
        'S': '⠠⠎', 'T': '⠠⠞', 'U': '⠠⠥', 'V': '⠠⠧', 'W': '⠠⠺', 'X': '⠠⠭',
        'Y': '⠠⠽', 'Z': '⠠⠵',
        '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢',
        '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔',
        ',': '⠂', '.': '⠲', '?': '⠦', '!': '⠖', "'": '⠄', '"': '⠐⠄',
        '-': '⠤', '_': '⠤', '(': '⠦⠴', ')': '⠴⠦', '&': '⠯', ';': '⠆⠂',
        ':': '⠒⠒', '/': '⠲⠆', '\\': '⠲⠆', '@': '⠈⠹',
        ' ': ' '
    }
    
    braille_text = ''
    for char in text:
        if char in braille_dict:
            braille_text += braille_dict[char]
    
    return braille_text


if __name__ == '__main__':
    app.run(debug=True)